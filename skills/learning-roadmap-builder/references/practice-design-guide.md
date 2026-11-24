# Deliberate Practice Design Guide

Great roadmaps fail when practice is vague ("read Chapter 3", "practice speaking"). Use this guide to design **domain-native, personalized, verifiable practice** for every week.

## 1. The 5-Stage Practice Architecture

Every `Week-NN-Practice.md` follows this progression (scaled to the user's weekly hours):

1. **Warm-Up Retrieval (5–10% time)** — 2–3 quick closed-book prompts revisiting Week `N-1` / `N-3` (spaced repetition).
2. **Guided Practice (25–30% time)** — 1–2 structured exercises with a worked example or step-by-step scaffold and clear expected outcome.
3. **Deliberate Drills (30–35% time)** — 2–3 targeted exercises isolating the week's hardest sub-skills at the edge of the learner's ability, tailored to their real-world context.
4. **Transfer Challenge (20–25% time)** — 1 realistic, unguided scenario combining the week's skills (plus earlier weeks in Phase 2+) with **hidden hints** (`<details>`) and an **Observable Rubric**.
5. **Feedback, Reflection & Error Log (10% time)** — Self-check rubric, an **AI Critique Prompt** (for solo learners), and a 3-line error/insight log.

## 2. Domain-Native Practice Menu

Pick exercises that match the learner's **Domain Archetype** — never force IT labs onto non-IT topics:

| Archetype | Guided Practice | Deliberate Drills | Transfer Challenge | Verification / Rubric |
| :--- | :--- | :--- | :--- | :--- |
| **Technical / Tooling** | Step-by-step lab / setup with expected output | Coding katas, debug broken config/code, refactor under constraints | Build a feature/architecture from spec without steps; break-and-fix | Automated tests, output check, cost/cleanup check |
| **Exam / Academic** | Worked problem walkthrough (show reasoning) | Concept-discrimination drills (A vs B traps), timed mini-sets | Mixed-domain timed quiz + explain *why* wrong options fail | Accuracy %, time/question, Weak-Area Error Log |
| **Foreign Language** | Shadowing / sentence-mining / model paragraph dissection | 10-min SRS flashcards, grammar transformation, timed 2-min monologue | Real-world communicative task (email, pitch, AI roleplay conversation) | CEFR-style rubric (fluency, accuracy, range, pronunciation) |
| **Creative / Craft** | Master study / teardown (analyze *why* a great piece works) | Constrained micro-drills (e.g. 5 headlines in 10m, 3 layouts, 1 technique) | Original mini-brief with audience, constraints, and deadline | Craft rubric (clarity, composition, originality, brief fit) |
| **Business / Knowledge** | Guided framework application on a famous case | Real-company teardown, back-of-the-envelope estimation, Feynman 1-pager | Decision memo / pitch under ambiguity with trade-offs | Logic, evidence quality, risk awareness, clarity |
| **Physical / Soft Skills** | Slow-motion / isolated mechanic drill with cue checklist | Scripted roleplay, timed drill, recorded 2-min delivery | Low-stakes real-world rep (real meeting, real conversation, live run) | Video/audio self-review rubric + post-rep debrief |

## 3. Adapting Practice to Learner Profile

### By Session Rhythm
- **Daily micro-sessions (20–30 min/day)**: Break the practice file into `Day 1` → `Day 5` atomic 20-min blocks (e.g. Mon: Warm-up + Concept; Tue–Thu: 1 Drill/day; Fri: Challenge; Sat: Review).
- **Weekday evenings (1h × 3–4)**: Group into 3–4 focused sessions (Understand + Guided → Drills → Challenge + Reflect).
- **Weekend deep blocks (2–3h × 2)**: Combine into 1 deep workshop (Theory + Guided + Drills) + 1 capstone lab/challenge session.

### By Verified Level
- **Beginner**: More worked examples, explicit step-by-step checklists, smaller scope, immediate wins in Week 1 to build confidence.
- **Intermediate**: Cut setup hand-holding; emphasize debugging, edge cases, comparing trade-offs, and realistic messy scenarios.
- **Advanced**: Focus on critique, optimization, synthesis across domains, teaching/explaining (Feynman), and real-world high-stakes deliverables.

### By Constraints
- **Zero budget**: Use only free tools, open datasets, free tiers, paper/pen, phone recorder, or AI roleplay. Flag any optional paid resource clearly.
- **Solo learner (no mentor/peer)**: Always include a copy-pasteable **AI Critique / Roleplay Prompt** in the practice file so the learner can get instant, rubric-based feedback.
- **Busy week (Minimum Viable Week)**: Mark exactly **1 core drill** with `[MVW]` so the learner knows the single highest-leverage exercise to complete when short on time.

## 4. Observable Rubric & AI Critique Prompt Pattern

For any open-ended practice (writing, speaking, design, business, architecture, craft), include:

1. **3–5 Observable Criteria** (binary or 1–3 scale — no vague "looks good"):
   - Example (Business memo): *States recommendation in the first 3 lines; backs claim with ≥2 concrete data points; addresses the #1 counterargument.*
   - Example (Language speaking): *Speaks ≥2 min without pausing >5s; uses ≥3 target connectors; self-corrects at most twice.*
2. **Copy-Paste AI Critique Prompt**:
   > *"Act as a strict [domain] coach. Evaluate my work below against these criteria: [list criteria]. Give: (1) Score per criterion (1–3), (2) Top 2 strengths, (3) Top 2 specific fixes with rewritten/concrete examples, (4) One follow-up drill for my weakest point."*

## 5. Conditional Sections (Include ONLY When Relevant)

- **Environment Setup & Prerequisites**: Technical, creative software, or physical equipment/space. Skip for pure reading/thinking topics.
- **Cost Warning & Resource Cleanup**: Cloud, paid APIs, or consumable materials. Omit completely for free/non-cloud domains.
- **Safety / Warm-up**: Physical skills, fitness, instruments.
