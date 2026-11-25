#!/usr/bin/env python3
"""Validate Agent Skills structure, frontmatter, progressive disclosure, and Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
MAX_SKILL_MD_LINES = 150

FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*\S+", re.MULTILINE)
MD_LINK_RE = re.compile(r"\]\(([^)#:\s]+\.md)(?:#([^)\s]*))?\)")
HTML_ID_RE = re.compile(r"<a\s+(?:id|name)=\"([^\"]+)\"", re.IGNORECASE)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
TEMPLATE_PLACEHOLDERS = ("<", "Week-NN", "Tuan-NN", "1.<")


def validate_skills() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not SKILLS_DIR.is_dir():
        errors.append("Missing required 'skills/' directory.")
        return errors, warnings

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        errors.append("No skill directories found under 'skills/'.")
        return errors, warnings

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
            continue

        text = skill_md.read_text(encoding="utf-8")
        lines = text.splitlines()

        fm_match = FRONTMATTER_RE.match(text)
        if not fm_match:
            errors.append(f"{skill_md.relative_to(ROOT)}: missing or malformed YAML frontmatter")
            continue

        frontmatter = fm_match.group(1)
        name_match = NAME_RE.search(frontmatter)
        if not name_match:
            errors.append(f"{skill_md.relative_to(ROOT)}: missing valid lowercase hyphenated 'name:'")
        elif name_match.group(1) != skill_dir.name:
            errors.append(
                f"{skill_md.relative_to(ROOT)}: frontmatter name '{name_match.group(1)}' "
                f"does not match directory '{skill_dir.name}'"
            )

        if not DESC_RE.search(frontmatter):
            errors.append(f"{skill_md.relative_to(ROOT)}: missing 'description:' in frontmatter")

        if len(lines) > MAX_SKILL_MD_LINES:
            warnings.append(
                f"{skill_md.relative_to(ROOT)}: {len(lines)} lines exceeds recommended "
                f"{MAX_SKILL_MD_LINES}-line progressive disclosure guideline"
            )

    return errors, warnings


def github_slug(heading: str) -> str:
    """Approximate GitHub heading anchors: lowercase, drop punctuation, spaces to hyphens."""
    text = re.sub(r"[`*_]", "", heading.strip().lower())
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s", "-", text)


def collect_anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    anchors = set(HTML_ID_RE.findall(text))
    anchors.update(github_slug(h) for h in HEADING_RE.findall(text))
    return anchors


def validate_markdown_links() -> list[str]:
    errors: list[str] = []
    md_files = sorted(
        p for p in ROOT.rglob("*.md") if ".git" not in p.parts
    )

    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        for match in MD_LINK_RE.finditer(text):
            rel = match.group(1)
            fragment = match.group(2)
            if any(token in rel for token in TEMPLATE_PLACEHOLDERS):
                continue
            target = (md_file.parent / rel).resolve()
            if not target.exists():
                errors.append(
                    f"{md_file.relative_to(ROOT)}: broken relative link -> '{rel}'"
                )
            elif fragment and fragment not in collect_anchors(target):
                errors.append(
                    f"{md_file.relative_to(ROOT)}: missing anchor '#{fragment}' in '{rel}'"
                )

    return errors


def main() -> int:
    errors, warnings = validate_skills()
    errors.extend(validate_markdown_links())

    for warning in warnings:
        print(f"WARN:  {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"\nValidation failed with {len(errors)} error(s).")
        return 1

    skill_count = sum(1 for p in SKILLS_DIR.iterdir() if p.is_dir())
    print(f"Validation passed: {skill_count} skills checked, 0 broken links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
