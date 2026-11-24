---
name: active-recall-quizzer
description: >-
  Use this skill when the user wants to test their memory, check knowledge gaps,
  run a diagnostic quiz, practice exam questions, or do spaced-repetition review
  on any subject (e.g. "quiz me on X", "test my understanding of Week 2", "tạo
  bài kiểm tra ôn tập Y", "run flashcards for Z"). Delivers adaptive, closed-book
  retrieval questions across Bloom's taxonomy, explains why wrong options fail,
  tracks weak areas, and schedules spaced reviews. Do not use for open-ended
  work critique or roleplay (use practice-critique-coach).
---

# Active Recall Quizzer

Strengthens long-term retention through **closed-book retrieval practice, adaptive
difficulty, discrimination drills, and spaced repetition** for any subject.

**Core rules:**
1. **One question (or small batch of 3–5) at a time.** Never dump 20 questions with answers visible right below — that ruins the testing effect.
2. **Test understanding, not trivia.** Prioritize scenario, comparison, and "spot the flaw" questions over rote definition matching.
3. **Explain the distractors.** When reviewing an answer, explain *both* why the right answer works and why the chosen wrong answer fails.

## Step 1 — Set Quiz Parameters

Check if the user already specified scope (or read the current week's notes if inside a
roadmap repo). Otherwise confirm quickly (1 short call or inline):
- **Scope**: specific topic, specific week(s), or mixed cumulative review?
- **Mode**:
  - **Interactive Tutor Quiz** (1 question at a time, adaptive difficulty — best for learning)
  - **Timed Mini-Mock** (5–15 questions in one batch, graded at the end — best for exam prep)
  - **Rapid Flashcards / SRS Review** (short recall prompts + self-rating: *Again / Hard / Good / Easy*)
- **Format**: Multiple choice · Short free-response · Scenario/Case · Mixed.

Match the user's language. Refer to [question-design-and-srs.md](./references/question-design-and-srs.md).

## Step 2 — Run the Retrieval Session

- **Start at baseline**, then adapt dynamically:
  - 2 correct in a row → step up Bloom's level (Recall → Application → Analysis/Edge Case).
  - Wrong or "I don't know" → step down briefly, give a concise explanation + mental hook, and **re-test the same concept in a fresh disguise** 2–3 questions later.
- **Interleave**: when reviewing multiple topics or weeks, mix questions randomly instead of grouping by chapter (forces discrimination).
- **Confidence check** *(optional for exam prep)*: ask the learner to tag answers as *Sure / Guessed* — a confident wrong answer is the highest-priority gap.

## Step 3 — Score, Diagnose & Schedule Spaced Review

At the end of the session, output:
1. **Scorecard by Sub-Topic** (Correct / Total · % · Status: Strong / Review / Priority Gap).
2. **Top Weak Areas & Root Causes** (misconception vs memory slip vs exam trap).
3. **Spaced-Repetition Schedule** (Leitner intervals: `1d → 3d → 7d → 14d → 30d`) for missed items.
4. **Next-Step Action**:
   - Offer to save/update a `weak-areas-log.md` (if in a study workspace).
   - Recommend either a 5-minute Socratic repair (`socratic-tutor`) on the #1 gap or a targeted drill (`practice-critique-coach`).
