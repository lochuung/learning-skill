# File Templates

Replace `<...>`. Use zero-padded week prefixes (`Week-01-` for English, `Tuan-01-` for Vietnamese) in ASCII hyphenated filenames so they sort cleanly. URL-encode spaces (`%20`) and `&` (`%26`) in Markdown links. Adapt headings to the user's language.

---

## 1. Master Roadmap (`README.md`)

````markdown
# Learning Roadmap: <TOPIC>

> **Goal (Definition of Done):** <concrete observable outcome> in **<N> weeks** (<h> hrs/week, <session shape>).

## 👤 Learner Profile & Personalization
- **Background & Analogies:** <role/field + adjacent skills used as analogies>
- **Domain Archetype:** <Archetype>
- **Verified Level:** <level> *(Diagnostic: x/y)*
- **Personalization Decisions:**
  - **Compressed / Skipped:** <topics already known>
  - **Extended / Emphasized:** <weak spots or high-weight areas>
  - **Constraints Respected:** <budget, tools, language, drop-off protection>

## 🎯 Curriculum & Outcome Map
| Domain / Skill Area | Weight / Priority | Target Mastery | Weeks |
| :--- | :---: | :--- | :---: |
| ... | ... | ... | W1–W2 |

*Reference / Syllabus:* [<Source Name>](<verified-url>)

## 🗺️ <N>-Week Roadmap

### Phase 1 — <Phase Name> (Weeks a–b)

#### Week 1 — <Title>
- **Objective:** <what the learner can DO by the end of this week>
- **Notes:** [Week-01-<Title>.md](1.<Phase>/Week-01-<Title>.md)
- **Practice:** [Week-01-Practice.md](1.<Phase>/Week-01-Practice.md)
- **Stages → Labs:** S1 → [Lab 1](1.<Phase>/Week-01-Practice.md#lab-1) · S2 → [Lab 2](1.<Phase>/Week-01-Practice.md#lab-2) `[MVW]` · S3 → [Lab 3](1.<Phase>/Week-01-Practice.md#lab-3) · S4 → [Lab 4](1.<Phase>/Week-01-Practice.md#lab-4)
- **Core Resource:** [<Name>](<url>)
- **Minimum Viable Week (MVW):** <30–40% fallback if busy>

| Concept / Sub-skill | Key Focus |
| :--- | :--- |
| ... | ... |

- **Practice Highlights:** <2–3 bullets of domain-native exercises>
---
*(Repeat per week; include review/buffer weeks where scheduled.)*

## 📅 Sample Weekly Schedule
<Table fitted to the user's actual session shape — daily 25m OR weekday 1h OR weekend blocks>

## 🧠 4-Step Learning Loop
1. **Understand** — Grasp the mental model & analogy.
2. **Visualize & Connect** — Diagram, table, or real-world teardown.
3. **Deliberate Practice** — Guided → Drill → Transfer Challenge + Rubric.
4. **Retrieve & Reflect** — Closed-book recall, error log, spaced review.

*(Include 1 concrete worked example tailored to <TOPIC>.)*

## 📚 Curated Resources
*(Grouped by Free / Optional Paid; every URL verified from Step 2.)*

## ✅ Progress Tracker
- [ ] **Week 1** — <Title> ([Notes](...) | [Practice](...))
- [ ] **Week 2** — ...
- [ ] **Final Milestone** — <Capstone / Mock Exam / Live Performance>

## 💡 Staying Consistent
- **Busy week?** Do the `[MVW]` drill only — never break the chain for >1 week.
- **Stuck?** Use the AI Critique Prompt inside each Practice file or review the Error Log.
````

---

## 2. Weekly Notes (`Week-NN-<Title>.md`)

Split every week into **3–4 Stages** (Vietnamese: **Chặng**). Each Stage teaches one focused concept cluster, checks it with 1–2 closed-book questions, and **ends with a pointer to the exact Lab** in `Week-NN-Practice.md` that practices it. Stage *k* ↔ Lab *k*, one-to-one. Never end a Stage without a Lab link, and never put two Stages before the same Lab.

````markdown
# Week N — <Title> (<TOPIC>)

> **By the end of this week, you can:** <2–3 concrete action outcomes (verbs, not "understand")>
> **Practice companion:** [Week-NN-Practice.md](Week-NN-Practice.md)

## 🗺️ Week Map (Stage → Lab)
| Stage | You will learn | Read | Lab (do right after) | Lab time |
| :-: | :--- | :-: | :--- | :-: |
| 1 | <concept cluster 1> | 15m | [Lab 1 — <Guided name>](Week-NN-Practice.md#lab-1) | 25m |
| 2 | <concept cluster 2> | 15m | [Lab 2 — <Drill A name>](Week-NN-Practice.md#lab-2) `[MVW]` | 25m |
| 3 | <concept cluster 3> | 15m | [Lab 3 — <Drill B name>](Week-NN-Practice.md#lab-3) | 30m |
| 4 | <integration> | 10m | [Lab 4 — Transfer Challenge](Week-NN-Practice.md#lab-4) | 45m |

> **Loop for every Stage:** Read → Checkpoint (closed-book) → Lab → back to the next Stage.

---

<a id="stage-1"></a>
## Stage 1 — <Concept cluster name>
> **Stage goal:** you can <verb + observable result>.

- **Why it matters:** <relevance to learner's goal>
- **Analogy from your background:** <tailored bridge>
- **How it works:** <concise explanation + comparison table or Mermaid diagram>
- **Worked example:** <concrete scenario in learner's context>
- **Watch out:** <1–2 pitfalls specific to this Stage>

### ✅ Stage 1 Checkpoint *(closed-book, 1–2 questions, 3 min)*
**Q:** <scenario or explain-in-your-own-words prompt>
<details>
<summary>Show answer</summary>
<concise answer + reasoning>
</details>

### 🧪 Next: Lab 1
> 👉 **Do now:** [Lab 1 — <Guided name>](Week-NN-Practice.md#lab-1) (~25 min)
> **What this lab proves:** <the Stage 1 skill it exercises>
> **Done when:** <observable completion criterion>. Then continue to Stage 2.

---

<a id="stage-2"></a>
## Stage 2 — <Concept cluster name>
*(Same structure: goal → concepts → Checkpoint → 🧪 Next: Lab 2. Mark the `[MVW]` lab here.)*

<a id="stage-3"></a>
## Stage 3 — <Concept cluster name>
*(Same structure → 🧪 Next: Lab 3.)*

<a id="stage-4"></a>
## Stage 4 — Integrate & Apply
*(Combine Stages 1…N-1; no new theory beyond a short synthesis → 🧪 Next: Lab N = Transfer Challenge.)*

---

## Common Pitfalls & Key Takeaways *(or Exam Traps for cert tracks)*
1. **Pitfall:** ... → **Instead:** ...

## Active Recall Check *(Closed-Book, after all Labs)*
*(5–8 questions: 4–6 from this week + 1–2 spaced-repetition callbacks from earlier weeks.)*

**Q1:** <question>
<details>
<summary>Show answer</summary>
<answer>
</details>
````

Rules:
- **3–4 Stages per week**, ~10–20 min reading each, matched to the learner's session length (a 25-min daily learner reads 1 Stage + does its Lab per day).
- Every Lab link uses an explicit anchor (`#lab-1`, `#lab-2`, …) that **exists** in the Practice file, and every Stage heading has a matching `<a id="stage-k"></a>` anchor so the Practice file can link back.
- The Stage that contains the `[MVW]` lab must say so in its "Next" box.

---

## 3. Weekly Deliberate Practice (`Week-NN-Practice.md`)

Organized as **Labs numbered to match the Stages** in the notes. Each Lab declares which Stage it covers and links back. Place an explicit `<a id="lab-k"></a>` anchor before each Lab heading (more reliable than auto-generated heading slugs).

````markdown
# Week N — Deliberate Practice: <Title>

> **Estimated time:** <X hrs> (fits your <session shape>) | **MVW time:** <Y mins>
> **Related notes:** [Week-NN-<Title>.md](Week-NN-<Title>.md)

## 🗺️ Lab Map
| Lab | Type | Covers | Time | Tag |
| :-: | :--- | :--- | :-: | :-: |
| [Lab 1](#lab-1) | Guided Practice | [Stage 1](Week-NN-<Title>.md#stage-1) | 25m | |
| [Lab 2](#lab-2) | Deliberate Drill A | [Stage 2](Week-NN-<Title>.md#stage-2) | 25m | `[MVW]` |
| [Lab 3](#lab-3) | Deliberate Drill B | [Stage 3](Week-NN-<Title>.md#stage-3) | 30m | |
| [Lab 4](#lab-4) | Transfer Challenge | Stages 1–3 | 45m | |

## 0. Prep & Setup *(Include ONLY if tools, materials, or cost apply; omit otherwise)*
> **Cost / Safety note:** <only if applicable>

## 1. Warm-Up Retrieval (5–10 min)
*(2–3 quick recall prompts from Week N-1 / N-3 — do closed-book before Lab 1.)*

---

<a id="lab-1"></a>
## Lab 1 — Guided Practice: <Name>
> **Covers:** [Stage 1 — <name>](Week-NN-<Title>.md#stage-1) | **Time:** 25 min
- **Goal:** ...
- **Steps / Scaffold:** <worked walkthrough or structured template>
- **Expected outcome:** <what good looks like>
- **Next:** continue to [Stage 2](Week-NN-<Title>.md#stage-2) in the notes.

<a id="lab-2"></a>
## Lab 2 `[MVW]` — Deliberate Drill A: <Targeted sub-skill>
> **Covers:** [Stage 2 — <name>](Week-NN-<Title>.md#stage-2) | **Time:** 25 min
- **Scenario (tailored to your context):** ...
- **Task:** ...
- **Target / Check:** ...

<a id="lab-3"></a>
## Lab 3 — Deliberate Drill B: <Targeted sub-skill>
> **Covers:** [Stage 3 — <name>](Week-NN-<Title>.md#stage-3)
...

<a id="lab-4"></a>
## Lab 4 — Transfer Challenge (Unguided)
> **Covers:** Stages 1–3 combined (plus earlier weeks in Phase 2+)
### Scenario & Constraints
<Realistic problem combining this week's skills without step-by-step instructions>

<details>
<summary>Hints (open only if stuck >15 min)</summary>
<progressive hints>
</details>

### Self-Check Rubric
| Criterion | 1 (Needs work) | 2 (Solid) | 3 (Strong) |
| :--- | :--- | :--- | :--- |
| <Observable criterion 1> | ... | ... | ... |
| <Observable criterion 2> | ... | ... | ... |
| <Observable criterion 3> | ... | ... | ... |

### AI Critique / Roleplay Prompt *(For solo feedback)*
> Copy & paste this prompt with your work into an AI assistant:
> "Act as a strict <domain> coach. Evaluate my work below against the rubric above (<list criteria>). Return: (1) Score 1–3 per criterion, (2) Top 2 strengths, (3) Top 2 concrete improvements with examples, (4) One 10-minute follow-up drill."

---

## Cleanup *(Include ONLY for cloud/paid/physical setups; omit otherwise)*

## Weekly Reflection & Error Log (3 min)
- **What clicked easily:** ...
- **What tripped me up (revisit next week):** ...
- **Checklist:**
  - [ ] Completed Warm-Up Retrieval
  - [ ] Completed Lab 1 and Lab 2 `[MVW]`
  - [ ] Completed Lab 3
  - [ ] Completed Lab 4 (Transfer Challenge) & scored rubric
  - [ ] Completed the Active Recall Check in the notes
````

Rules:
- Lab count equals Stage count; Lab *k* covers Stage *k*, and the last Lab is the Transfer Challenge.
- Exactly one Lab carries `[MVW]`.
- The Transfer Challenge's rubric and AI Critique Prompt live inside the last Lab.

---
## 4. Final-Phase Variants (Choose Matching Track)

### Track A — Exam / Certification
- `Week-NN-Consolidation.md`: Cross-domain integration scenarios / mindmap + 5 defense questions.
- `Week-NN-Mock-Exam-and-Weak-Areas.md`: Timed simulation instructions, ≥25 scenario questions grouped by domain with `<details>` rationales, **Weak-Area Tracker** table (Domain · Score · % · Link back to week).
- `Week-NN-Cheat-Sheet-and-Readiness.md`: 7-day countdown plan, key numbers/formulas/rules, keyword→answer triggers, exam-day tactics, Go/No-Go readiness checklist.

### Track B — Project / Portfolio / Capstone (Technical, Creative, Business)
- `Week-NN-Capstone-Brief.md`: Real-world project specification tailored to learner's goal, scope boundaries (MVP vs stretch), milestone checklist.
- `Week-NN-Review-Rubric-and-Defense.md`: Detailed quality rubric, self-review / AI-review prompt, 5–8 "defense questions" (why did you choose X over Y?), portfolio presentation guide, and next-90-day growth plan.

### Track C — Fluency / Live Performance (Language, Soft Skills, Physical)
- `Week-NN-Simulation-and-Dress-Rehearsal.md`: Realistic timed simulation / roleplay script / live performance brief with recording checklist.
- `Week-NN-Assessment-and-Maintenance.md`: Competency self-assessment rubric (before vs after comparison), real-world deployment challenge, and a sustainable 15-min/day maintenance routine so skills don't decay.

### Sprint Variant (≤4 Weeks)
Collapse to 2 phases and use a **single combined file per week** (`Week-NN-<Title>.md`) with 2–3 Stages. Each Stage holds concise theory, a Checkpoint, and an **inline Lab** at its end (### 🧪 Lab k), and the last Stage's Lab is the Mini-Challenge + Rubric.
