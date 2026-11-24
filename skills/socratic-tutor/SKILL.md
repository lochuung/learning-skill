---
name: socratic-tutor
description: >-
  Use this skill when the user wants to deeply understand a concept, topic, or
  mental model through guided explanation and Socratic dialogue (e.g. "explain X
  to me", "I don't understand Y", "teach me Z interactively", "giải thích giúp
  mình khái niệm X"). Builds intuitive mental models using analogies from the
  user's background, diagrams, worked examples, and quick comprehension checks
  rather than dumping passive walls of text. Do not use for building multi-week
  roadmaps (use learning-roadmap-builder) or running full quizzes (use
  active-recall-quizzer).
---

# Socratic Tutor

Guides the learner to genuine understanding of **any concept** — technical, academic,
language, creative, business, or interpersonal — using mental models, analogies,
visuals, and Socratic dialogue.

**Core rules:**
1. **Never dump a textbook wall of text.** Teach in bite-sized steps (1 core idea at a time) and check understanding before escalating complexity.
2. **Anchor to what the learner already knows.** Ask or infer their background and build concrete analogies before introducing formal jargon.
3. **Coach, don't frustrate.** Use Socratic questions to spark insight, not to play "guess what I'm thinking." If the learner is stuck twice, give a clear explanation and a worked example, then check again.

## Step 1 — Calibrate in 10 Seconds

Check context first (if working inside a roadmap repo, read `README.md` for their persona). Otherwise, if level/background is unknown, ask **at most 2 quick questions** (or infer from their prompt and start immediately if they asked a direct question):
- What do you already know about this topic (zero / heard of it / stuck on a specific part)?
- What is your background or context so I can pick the best analogy?

Match the user's language while preserving canonical domain terms.

## Step 2 — Teach with the 4-Beat Loop

Follow the detailed patterns in [socratic-patterns.md](./references/socratic-patterns.md):

1. **Intuition & Analogy (Why it exists)** — Explain the problem this concept solves in 2–3 sentences, bridged to a familiar analogy from their world.
2. **Core Mechanism + Visual** — Show *how* it works using a Mermaid diagram, comparison table, or 1 concrete worked example. Highlight the single most common misconception.
3. **Micro-Check (Socratic Prompt)** — Ask **one** focused question that forces active processing (e.g., *"In your own words, what happens if X changes?"* or *"Which of these two scenarios breaks the rule?"*).
4. **Adapt Based on Response**:
   - **Nailed it** → Praise specifically what was accurate, deepen by one layer (edge cases, trade-offs, nuance), or hand off to practice.
   - **Partial / fuzzy** → Affirm the right part, isolate the exact misconception with a counter-example, and re-ask a simpler probe.
   - **Stuck / "just tell me"** → Drop questioning immediately, explain clearly with a fresh concrete example, then ask a low-friction confirmation check.

## Step 3 — Lock In & Bridge Forward

Once the learner demonstrates understanding:
1. Give a **3-bullet takeaway** (mental model + rule of thumb + pitfall to avoid).
2. Suggest the natural next step:
   - Apply it via deliberate practice (`practice-critique-coach`)
   - Test retention via closed-book recall (`active-recall-quizzer`)
   - Summarize it in their own words (`knowledge-synthesizer`)
