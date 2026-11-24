---
name: knowledge-synthesizer
description: >-
  Use this skill when the user wants to consolidate, distill, or turn messy
  study notes, articles, books, videos, or a completed week into durable
  knowledge using the Feynman Technique, atomic notes, comparison matrices,
  concept maps, or cheat sheets (e.g. "help me Feynman-explain X", "turn my
  notes into a cheat sheet", "build a concept map for Y", "tổng hợp kiến thức
  tuần này"). Focuses on active synthesis and exposing hidden gaps rather than
  passive copy-paste summarizing. Do not use for multi-week roadmap creation
  (use learning-roadmap-builder).
---

# Knowledge Synthesizer

Transforms raw information (readings, lectures, messy notes, completed weeks) into
**clear, durable, connected knowledge** using the Feynman Technique, visual mapping,
and high-density reference sheets.

**Core rules:**
1. **Synthesis beats summarization.** Don't just shorten text — reorganize by mental models, expose relationships, contrast confusable ideas, and strip fluff.
2. **Prefer learner-first Feynman.** When the user wants to truly internalize a topic, invite them to explain it in plain words *first*, then expose gaps and co-refine — instead of doing all the thinking for them.
3. **One page = one clear purpose.** Every output should be scannable in 60 seconds during future revision.

## Mode Selection

Match the user's language and pick the right mode (templates in
[synthesis-templates.md](./references/synthesis-templates.md)):

### Mode A — Interactive Feynman Teach-Back (Deepest Retention)
1. Ask the learner to explain the topic in **plain language** (as if teaching a smart 12-year-old or a colleague from another field) in 5–10 lines — no jargon allowed without defining it.
2. **Audit their explanation**:
   - Highlight what they explained clearly and accurately.
   - Flag **jargon masks** (words used without explaining the mechanism) and **logic leaps** (missing "why/how" links).
   - Ask 1–2 probing questions to help them patch the gaps.
3. Co-produce a clean, finalized **Atomic Concept Note** they can save in their study repo.

### Mode B — Distill Notes / Source into Structured Artifacts
When the user provides notes, a chapter, an article, or a completed roadmap week,
generate the requested artifact (or recommend the best fit):
- **Atomic Concept Note** — 1 core idea, plain explanation, analogy, worked example, pitfalls, links to related concepts.
- **Comparison Matrix** — side-by-side table separating 2–5 commonly confused concepts (when to use, trade-offs, classic trap).
- **Concept Map (Mermaid)** — visual diagram showing hierarchy, cause-and-effect, or decision flow across a module/phase.
- **One-Page Cheat Sheet** — ultra-dense revision sheet (key rules/formulas/thresholds, decision tree, keyword → action triggers, top pitfalls).

## Output & Repo Integration

- Keep prose tight: bullets, tables, and diagrams over long paragraphs.
- If working inside a study/roadmap workspace, offer to save the synthesized note into the appropriate week or `cheat-sheets/` folder and link it cleanly.
- End by suggesting 2–3 quick **Active Recall** prompts (or handing off to `active-recall-quizzer`) to verify the synthesized knowledge actually sticks.
