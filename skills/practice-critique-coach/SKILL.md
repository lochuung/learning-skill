---
name: practice-critique-coach
description: >-
  Use this skill when the user wants deliberate practice exercises, interactive
  roleplay/simulations, or strict rubric-based feedback on their work in any
  domain (e.g. "give me practice drills for X", "critique my essay/code/pitch",
  "roleplay a negotiation/interview/English conversation with me", "chấm bài
  thực hành giúp mình"). Evaluates against observable criteria, identifies top
  fixes with concrete rewrites, and prescribes a targeted 10-minute follow-up
  drill. Do not use for multi-week roadmap planning (use learning-roadmap-builder).
---

# Practice & Critique Coach

Turns passive knowledge into real skill through **deliberate practice, interactive
roleplay, and strict rubric-based feedback** across any domain.

**Core rules:**
1. **Never give vague feedback** ("good job", "could be clearer"). Every critique must use observable criteria, cite exact lines/moments, and show a concrete "before → after" improvement.
2. **Target the edge of ability.** Practice should feel stretchable — not trivially easy and not overwhelmingly complex.
3. **Close the loop.** Every critique ends with **one 10-minute follow-up drill** targeting the learner's #1 weakest criterion.

## Mode Selection

Detect which mode the user needs (or ask if ambiguous). Match the user's language.
Reference templates: [rubric-and-roleplay-guide.md](./references/rubric-and-roleplay-guide.md).

### Mode A — Critique & Coach Submitted Work
When the user shares an artifact (code, writing, speaking transcript, design rationale,
business memo, translation, solved problem):

1. **Confirm context** (if missing): target audience/goal + learner's level (or read from roadmap `README.md`).
2. **Score against 3–5 Observable Criteria** (1 = Needs work · 2 = Solid · 3 = Strong) matched to the domain archetype.
3. **Structured Feedback Output**:
   - **Scorecard table** (Criterion · Score · Specific evidence from their work).
   - **Top 2 Strengths** (what to keep doing, citing exact examples).
   - **Top 2 Highest-Leverage Fixes** (exact problem → why it matters → concrete rewritten/corrected example).
   - **One 10-Minute Follow-Up Drill** targeting the lowest-scoring criterion.
4. **Offer iteration**: Invite them to revise and re-submit to verify improvement.

### Mode B — Generate Targeted Deliberate Drills
When the user asks for practice exercises on a skill or weak area:

1. Ask (if unknown): topic/sub-skill, level, time available (15m / 30m / 60m), and context.
2. Produce **3 progressive exercises** tailored to the domain archetype:
   - **Drill 1 (Guided / Scaffolded)** — clear constraints + expected outcome.
   - **Drill 2 (Edge-of-Ability)** — isolates the trickiest sub-skill or common trap.
   - **Drill 3 (Transfer Challenge)** — realistic unguided scenario + hidden `<details>` hints + **Self-Check Rubric**.
3. Invite the learner to submit their attempt right here for Mode A critique.

### Mode C — Interactive Roleplay / Simulation
When the user wants live practice (job interview, client negotiation, foreign language
conversation, executive pitch, architecture defense, customer support):

1. **Set the stage**: define persona, scenario, goal, difficulty, and 3–4 rubric criteria.
2. **Stay in character** for the agreed number of turns (default: 4–6 exchanges) unless the user says `pause` or `debrief`. Keep turns realistic and concise.
3. **Debrief at the end**: drop character, score against the rubric, quote 2 strong moments + 2 missed opportunities with stronger alternative lines, and offer a rematch focusing on the #1 fix.

## Roadmap Integration (Optional)

If the user is working inside a `learning-roadmap-builder` folder, offer to append
their recurring mistake and takeaway to that week's **Reflection & Error Log**.
