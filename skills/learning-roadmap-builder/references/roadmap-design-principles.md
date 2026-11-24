# Roadmap Design Principles

Evidence-based curriculum design applicable to **any** domain.

## 1. Backward Design (Outcome First)

Always design in reverse:
1. **Define observable mastery**: What concrete artifact, performance, or score proves success?
2. **Identify evidence**: What tasks/tests demonstrate that mastery?
3. **Map prerequisites & sub-skills**: Decompose into atomic skills ordered by dependency (foundational mental models → core mechanics → integration & edge cases → transfer to real life).
4. **Allocate time**: Budget weeks based on skill difficulty, official weightings (if exam), and learner gaps — not arbitrary equal splits.

## 2. Domain Archetypes

Classify the topic into one primary archetype (or a hybrid, e.g. *Technical + Exam*) to drive phase structure, notes, and practice:

| Archetype | Examples | Core Progression | Primary Practice Mode | Final Deliverable |
| :--- | :--- | :--- | :--- | :--- |
| **Technical / Tooling** | Coding, Cloud, Data, Excel, CAD | Mental models → Guided use → Debugging/Architecture → Production | Labs, katas, build-and-break, code/config reviews | Capstone project + architecture defense |
| **Exam / Academic** | IELTS, CFA, PMP, AWS, Uni courses | Syllabus foundations → High-weight domains → Timed drills & gap-closing | Active recall, spaced quizzes, timed mocks, error log | Full mock exam + weak-area closure + cheat sheet |
| **Foreign Language** | English, Japanese, French | Core sounds/grammar/vocab → Comprehensible input → Guided output → Fluency | Daily SRS + shadowing + reading/listening + writing/speaking roleplay | Recorded conversation / essay / proficiency mock |
| **Creative / Craft** | UX/UI, Writing, Photo, Music, Cooking | Principles & taste (deconstruction) → Micro-drills → Constrained briefs → Original work | Master studies, timed drills, iterative briefs + critique rubric | Portfolio piece(s) + process breakdown |
| **Business / Knowledge** | Finance, Marketing, PM, History, Law | Core frameworks → Case analysis → Decision-making under ambiguity → Application | Case studies, Feynman memos, teardowns, decision simulations | Strategy memo / real-world analysis / investment thesis |
| **Physical / Soft Skills** | Public speaking, Negotiation, Leadership, Fitness, Chess | Mechanics decomposition → Isolated drills → Simulated pressure → Live execution | Micro-drills, roleplay scripts, recorded rehearsal, real-world reps | Live performance / recorded showcase + reflection log |

## 3. Sizing & Pacing

- **Reality check**: `Total hours = weeks × hours/week`. Compare against realistic domain benchmarks (e.g., associate cert: 60–120h; functional beginner skill: 20–40h; CEFR level jump: 150–200h). If under-budgeted, **explicitly warn** the user and propose either extending duration or narrowing scope.
- **Cognitive load**: One week = one coherent theme (max 3–5 core concepts). Weekly workload must fit stated hours (+10% max).
- **Review buffers**: Insert 1 consolidation/review week every 4–5 weeks (especially for learners with <5h/week or high-memorization domains).
- **Minimum Viable Week (MVW)**: Define a 30–40% "busy-week fallback" (e.g., 1 core concept + 1 retrieval drill) so life disruptions never cause total drop-off.

## 4. Phase Architecture (Scale Proportionally)

- **Standard (6–16 weeks) — 3 Phases**:
  1. **Foundation (~25–35%)**: Mental models, vocabulary, core mechanics. *Shrink if diagnostic probes are strong.*
  2. **Core Application (~40–50%)**: High-weight skills, realistic scenarios, deliberate practice, combining sub-skills.
  3. **Integration & Mastery (~20–25%)**: End-to-end capstone, timed mocks, live performance, gap remediation, and next-step maintenance plan.
- **Sprint (≤4 weeks) — 2 Phases**:
  1. **Rapid Foundations & Core (60–70%)**: Combined notes + practice file per week.
  2. **Applied Capstone / Assessment (30–40%)**: Focused synthesis and verification.

## 5. Evidence-Based Learning Science Rules

Bake these into every roadmap:
1. **Active Recall (Testing Effect)**: Every note ends with retrieval questions (closed-book); every practice starts with a 3–5 min warm-up recall of prior weeks.
2. **Spaced Repetition**: Explicitly resurface concepts from Week `N-1` and `N-3` in Week `N`'s review questions and drills. For heavy-memory topics (vocab, formulas, terms), integrate SRS/flashcards.
3. **Interleaving**: From Phase 2 onward, mix problems from multiple sub-topics in practice instead of only drilling one concept in isolation.
4. **Scaffolding & Fading**: Progress within each week from *Worked Example* → *Guided Exercise* → *Faded Prompt* → *Independent Transfer Challenge*.
5. **Dual Coding & Elaboration**: Pair prose with diagrams/tables/timelines (Mermaid or structured tables) and connect every new concept to an analogy from the learner's background.
6. **Metacognition & Error Logging**: Require a 3-minute weekly reflection: *What clicked? What tripped me up? What 1 thing will I revisit?*

## 6. Universal 4-Step Weekly Loop

Apply to every topic regardless of field:
1. **Understand** — Core idea, why it matters, mental model, analogy to what you already know.
2. **Visualize & Connect** — Diagram, framework, comparison table, or deconstructed real-world example.
3. **Deliberate Practice** — Edge-of-ability exercises matched to the domain and session rhythm (see [practice-design-guide.md](./practice-design-guide.md)).
4. **Retrieve & Reflect** — Closed-book recall, self-assessment against rubric, error log, and spaced review.

## 7. Personalization Levers

- **Already known** → Compress to a "Checkpoint & Gap-Fill" half-week or skip via a 5-question verification quiz.
- **Weak spots / high-weight areas** → Extend duration, add extra deliberate drills, and schedule spaced callbacks.
- **Background analogies** → Translate unfamiliar concepts into the learner's native mental models (e.g., explaining cash flow to a software engineer via streaming buffers; explaining UX hierarchy to a writer via headline/subhead structure).
- **Session-rhythm fit** → Daily 20–30 min learners get micro-drills (Mon–Fri) + mini-synthesis (Sat); weekend-block learners get deep reading + extended project blocks.
- **Drop-off protection** → Address their stated failure mode directly (e.g., if they quit from boredom, lead with a concrete mini-project in Week 1; if they lack feedback, embed AI Critique Prompts in every practice file).
