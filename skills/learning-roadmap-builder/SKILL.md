---
name: learning-roadmap-builder
description: >-
  Use this skill when the user wants to learn any subject, skill, or field and asks
  for a personalized study plan, learning roadmap, curriculum, practice plan, or
  exam prep (e.g. "lập lộ trình học X", "plan to learn financial analysis", "study
  roadmap for IELTS 7.5", "learn Rust in 3 months", "master public speaking"). It
  interviews the user to diagnose level, goals, context, and constraints, classifies
  the domain archetype, and generates a personalized multi-phase Markdown repository
  with theory notes, domain-native deliberate practice, rubrics, and progress tracking.
  Do not use for one-off explanations of a single concept.
---

# Learning Roadmap Builder

Builds a personalized, evidence-based learning roadmap and deliberate practice repository
for **any domain** — technical, academic/exam, language, creative/craft, business/humanities,
or physical/soft skills.

**Core rules:**
1. **Never generate a roadmap before completing the interview (Step 1) and blueprint confirmation (Step 3).** A generic roadmap is a failed outcome.
2. **Practice must match the domain and the learner.** Never force coding/cloud labs onto non-technical subjects, and never give passive "read/watch" checklists without active recall and observable practice.
3. **Design backward from the outcome.** Every week's notes and practice must directly build toward what the learner actually wants to *do* or *prove*.

## Step 1 — Interview & Diagnose (Personalization)

Use `ask_question` (multiple choice, batch up to 4 related questions per call, max ~3 rounds).
Match the user's language. Skip questions already answered in the prompt.
Full question bank: [interview-guide.md](./references/interview-guide.md).

Collect at minimum:
1. **Topic & target outcome** — exact subject + what "done" looks like (pass an exam/score, perform at work, ship a portfolio piece, hold conversations, personal fluency) + deadline.
2. **Background & transfer anchors** — current role/field, adjacent skills or experiences they already have (used to build analogies and skip redundant basics).
3. **Verified level** — self-rating + **2–4 diagnostic probes** (concrete scenario/concept questions spanning easy → hard, with an "I don't know" option) to verify real baseline. If self-rating and probes conflict, trust the probes and state why.
4. **Time rhythm & duration** — hours/week, **session shape** (e.g. 20–30 min daily micro-sessions vs 2h weekend deep-work blocks), total duration preference (or let you recommend).
5. **Learning preferences & feedback** — theory-to-practice balance, preferred modalities (reading, visual, audio/video, writing, speaking/roleplay, hands-on), language of materials, solo vs mentor/peer/AI feedback.
6. **Constraints & drop-off risks** — budget, available tools/equipment/environment, past failed attempts, weak spots, and what usually causes them to stall.

Summarize the **Learner Persona** before moving on.

## Step 2 — Classify Domain & Research

1. **Classify the primary domain archetype** (can be hybrid, e.g. Technical + Exam) per [roadmap-design-principles.md](./references/roadmap-design-principles.md):
   - **Technical / Engineering / Tooling** (programming, cloud, data, Excel, CAD)
   - **Exam / Certification / Academic** (IELTS, CFA, PMP, AWS, university courses)
   - **Foreign Language** (English, Japanese, etc.)
   - **Creative / Design / Craft** (UI/UX, writing, photography, music, cooking)
   - **Business / Knowledge / Humanities** (finance, marketing, PM, psychology, history)
   - **Physical / Performance / Soft Skills** (public speaking, negotiation, leadership, chess, fitness)
2. **Research with `search_web`** to ground the curriculum in current reality:
   - Official syllabus, exam blueprint/weights, competency framework (e.g. CEFR, Bloom's, industry standards), or canonical learning progression.
   - Current authoritative free/paid resources, recent updates/deprecations, and realistic study-hour benchmarks.
   - Record source URLs to cite in `README.md`.

## Step 3 — Propose & Confirm the Blueprint

Present a **concise blueprint** (not full weekly files yet) and confirm via `ask_question`:
- **Persona summary** + **Domain archetype** + **Definition of Done** (final deliverable/milestone).
- **Sizing check**: total hours (`weeks × hours/week`) vs benchmark; warn if under-budgeted and suggest scope/duration trade-offs.
- **Phase structure & week-by-week table**: highlight which weeks are **compressed/skipped** (already known), **extended** (weak spots/high weight), or **review buffers**.
- **Practice model**: what weekly practice looks like for this domain and session rhythm (per [practice-design-guide.md](./references/practice-design-guide.md)), plus the **Minimum Viable Week (MVW)** fallback for busy weeks.
- **Generation scope**: confirm target folder (default: `<topic-slug>/` in workspace) and whether to generate **README + Week 1 first** (recommended for roadmaps >4 weeks so the user can test-drive and calibrate) or a full phase.

Iterate until approved.

## Step 4 — Generate the Repository

Use [templates.md](./references/templates.md) and [practice-design-guide.md](./references/practice-design-guide.md). Adapt file prefixes to the user's language (`Week-01-...` or `Tuan-01-...`, ASCII, hyphenated).

```text
<topic-slug>/
├── README.md                        # Master roadmap, persona, schedule, MVW, resources, tracker
├── 1.<Phase-1-Name>/
│   ├── Week-01-<Title>.md           # Concept notes + analogies + recall questions
│   ├── Week-01-Practice.md          # Domain-native deliberate practice + rubric + reflection
│   └── ...
├── 2.<Phase-2-Name>/ ...
└── 3.<Final-Phase-Name>/            # Exam Prep OR Capstone/Portfolio OR Live Performance
    └── ...
```

Generation rules:
- **README first**: learner profile & personalization decisions, outcome/syllabus map, phase & week breakdown, weekly schedule matched to their actual session rhythm, **Minimum Viable Week** rule, curated resources with verified URLs, the universal 4-step loop (**Understand → Visualize/Connect → Deliberate Practice → Retrieve & Reflect**), and a **Progress Tracker**.
- **Visible personalization**: weave analogies from the learner's background into notes; tailor scenarios/examples to their real job, industry, or personal goals; respect budget and tool constraints; write in their language while keeping canonical domain terms intact.
- **Notes (`Week-NN-<Title>.md`)**: learning objectives, key concepts explained clearly (not walls of text), comparison tables / Mermaid diagrams where helpful, common pitfalls / misconceptions, and 5–8 active-recall questions (including 1–2 spaced-repetition questions from earlier weeks) with collapsed `<details>` answers.
- **Practice (`Week-NN-Practice.md`)**: designed per [practice-design-guide.md](./references/practice-design-guide.md) — warm-up recall, progressive scaffolding (Guided → Deliberate Drill → Transfer Challenge), explicit **Self-Check Rubric**, **AI Critique Prompt** (so solo learners can get structured feedback), and a short **Reflection & Error Log**. Only include environment setup, cost notes, or cleanup when the domain actually requires them.
- **Final phase**: choose the matching capstone track — **(A) Exam/Cert** (consolidation, ≥25-question mock + weak-area tracker, cheat sheet), **(B) Project/Portfolio** (real-world capstone spec + rubric + review checklist), or **(C) Fluency/Performance** (live simulation/roleplay + recording rubric + ongoing maintenance plan).
- **Iterative delivery**: for roadmaps >4 weeks, generate `README.md` + Phase 1 (or Week 1–2) first, update links/tracker, and offer to continue or recalibrate difficulty/pace. Never claim files you did not write.
- **Factual accuracy**: verify facts, figures, frameworks, and links against Step 2 sources; mark anything uncertain.

## Step 5 — Validate & Hand Over

1. List all created files and verify every relative link in `README.md` resolves cleanly (URL-encode spaces as `%20`, `&` as `%26`).
2. Confirm every generated week has its notes + practice file (or combined file for ≤4-week sprints) and appears in the Progress Tracker.
3. Give a concise handover: folder structure, key personalizations applied, exact **Day 1 first action** (≤15 min to build momentum), and offer next actions (generate next weeks, run a diagnostic quiz, act as a practice/critique partner, or adjust pace).
