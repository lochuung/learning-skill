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

````markdown
# Week N — <Title> (<TOPIC>)

> **By the end of this week, you can:** <2–3 concrete action outcomes (verbs, not "understand")>
> **Practice companion:** [Week-NN-Practice.md](Week-NN-Practice.md)

## Table of Contents
1. ...

## 1. <Core Concept>
- **Why it matters:** <real-world relevance to learner's goal>
- **Analogy from your background:** <tailored bridge to what they already know>
- **How it works:** <concise explanation + comparison table or Mermaid diagram>
- **Worked example:** <concrete scenario in learner's context>

*(Repeat for 3–5 focused concepts — avoid walls of text.)*

## N-1. Common Pitfalls & Key Takeaways *(or Exam Traps for cert tracks)*
1. **Pitfall:** ... → **Instead:** ...

## N. Active Recall Check *(Closed-Book)*
*(5–8 questions: 4–6 from this week + 1–2 spaced-repetition callbacks from earlier weeks.)*

**Q1:** <scenario or explain-in-your-own-words prompt>
<details>
<summary>Show answer</summary>
<concise answer + reasoning>
</details>
````

---

## 3. Weekly Deliberate Practice (`Week-NN-Practice.md`)

````markdown
# Week N — Deliberate Practice: <Title>

> **Estimated time:** <X hrs> (fits your <session shape>) | **MVW time:** <Y mins>
> **Related notes:** [Week-NN-<Title>.md](Week-NN-<Title>.md)

## 0. Prep & Setup *(Include ONLY if tools, materials, or cost apply; omit otherwise)*
> **Cost / Safety note:** <only if applicable>

## 1. Warm-Up Retrieval (5–10 min)
*(2–3 quick recall prompts from Week N-1 / N-3 — do closed-book before starting.)*

## 2. Guided Practice: <Name>
- **Goal:** ...
- **Steps / Scaffold:** <worked walkthrough or structured template>
- **Expected outcome:** <what good looks like>

## 3. Deliberate Drills *(Pick 2–3; mark the #1 highest-leverage drill with `[MVW]`)*
### Drill A `[MVW]`: <Targeted sub-skill>
- **Scenario (tailored to your context):** ...
- **Task:** ...
- **Target / Check:** ...

### Drill B: <Targeted sub-skill>
...

## 4. Transfer Challenge (Unguided)
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

## 5. Cleanup *(Include ONLY for cloud/paid/physical setups; omit otherwise)*

## 6. Weekly Reflection & Error Log (3 min)
- **What clicked easily:** ...
- **What tripped me up (revisit next week):** ...
- **Checklist:**
  - [ ] Completed Warm-Up Retrieval
  - [ ] Completed `[MVW]` drill
  - [ ] Completed Transfer Challenge & scored rubric
````

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
Collapse to 2 phases and use a **single combined file per week** (`Week-NN-<Title>.md`) containing concise Notes + 1–2 Deliberate Drills + Mini-Challenge + Rubric.
