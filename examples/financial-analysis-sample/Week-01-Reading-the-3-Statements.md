# Week 1 — Reading the 3 Financial Statements Without Jargon (Financial Statement Analysis)

> **By the end of this week, you can:**
> - Trace one business transaction across the Income Statement, Balance Sheet, and Cash Flow Statement.
> - Explain why a profitable company can still run out of cash.
> - Write a 150-word cash-and-balance-sheet health snapshot of a public company.
>
> **Practice companion:** [Week-01-Practice.md](Week-01-Practice.md)

## 🗺️ Week Map (Stage → Lab)
| Stage | You will learn | Read | Lab (do right after) | Lab time |
| :-: | :--- | :-: | :--- | :-: |
| 1 | One transaction, three statements | 15 min | [Lab 1 — Trace One Transaction](Week-01-Practice.md#lab-1) | 25 min |
| 2 | Why cash ≠ profit | 15 min | [Lab 2 — Cash vs Profit Teardown](Week-01-Practice.md#lab-2) `[MVW]` | 25 min |
| 3 | Working capital warning signs | 15 min | [Lab 3 — Profitable but Dying Trap](Week-01-Practice.md#lab-3) | 30 min |
| 4 | Integrate: the Health Snapshot | 10 min | [Lab 4 — Transfer Challenge](Week-01-Practice.md#lab-4) | 45 min |

> **Loop for every Stage:** Read → Checkpoint (closed-book) → Lab → next Stage.

---

<a id="stage-1"></a>
## Stage 1 — One transaction, three statements
> **Stage goal:** you can say where a single sale shows up in each of the 3 statements.

- **Why it matters:** every later topic (margins, ROIC, valuation) reads numbers from these three statements. If you can't connect them, the numbers stay isolated facts.
- **Analogy from your background:** the Balance Sheet is a **snapshot of system state** at one moment. The Income Statement is a **log of events over a period**. The Cash Flow Statement is **real-time I/O throughput** of cash.
- **How it works:**

| Statement | Question it answers | Time view |
| :--- | :--- | :--- |
| Income Statement | Did the business earn money this period? | Period (video) |
| Balance Sheet | What does it own and owe right now? | Point in time (snapshot) |
| Cash Flow Statement | Where did cash actually come from and go? | Period (video) |

- **Worked example:** a customer pays \$120,000 upfront for a 12-month subscription on Jan 1. In January you have earned only 1/12 of it.
  - Income Statement: Revenue +\$10,000
  - Cash Flow Statement: Operating cash +\$120,000
  - Balance Sheet: Cash +\$120,000; Deferred Revenue (liability, service still owed) +\$110,000; Equity +\$10,000 (the earned revenue, before any costs)
- **Watch out:** "Revenue" is not "cash received". Revenue is recognized when the service is delivered, not when the money arrives.

### ✅ Stage 1 Checkpoint *(closed-book, 3 min)*
**Q:** In the example above, why is Deferred Revenue a *liability* even though the customer already paid?
<details>
<summary>Show answer</summary>

The company still owes 11 months of service. Until it delivers them, the cash it holds is matched by an obligation. Each month, \$10,000 moves from Deferred Revenue to Revenue.

</details>

### 🧪 Next: Lab 1
> 👉 **Do now:** [Lab 1 — Trace One Transaction](Week-01-Practice.md#lab-1) (~25 min)
> **What this lab proves:** you can place one event in all 3 statements and keep the Balance Sheet balanced.
> **Done when:** your three numbers (+\$10k revenue, +\$120k cash, +\$110k deferred revenue) match, and you can explain each. Then continue to Stage 2.

---

<a id="stage-2"></a>
## Stage 2 — Why cash ≠ profit
> **Stage goal:** you can name at least two reasons Net Income and Operating Cash Flow differ for a real company.

- **Why it matters:** companies report profit, but they pay bills with cash. Investors who read only the Income Statement miss this gap.
- **Analogy from your background:** Net Income is like *requests accepted* by a service, and Operating Cash Flow is like *requests completed and paid*. A queue can grow while the dashboard looks healthy.
- **How it works:** Operating Cash Flow starts from Net Income and adjusts for items that did not move cash:

| Adjustment | Direction on cash | Example |
| :--- | :-: | :--- |
| Depreciation & amortization | + | Expense reduced profit but no cash left this year |
| Stock-based compensation | + | Expense paid in shares, not cash |
| Increase in Accounts Receivable | − | Sold, but not collected yet |
| Increase in Deferred Revenue | + | Collected, but not yet earned |

- **Free Cash Flow (FCF)** = Operating Cash Flow − Capital Expenditures. It is the cash left after maintaining and growing the asset base.
- **Worked example:** Net Income \$100M, D&A +\$30M, stock comp +\$20M, receivables increase −\$40M → Operating Cash Flow \$110M. If CapEx is \$50M, FCF is \$60M.
- **Watch out:** a large gap between Net Income and OCF is a question to investigate, not automatically bad news. Deferred revenue growth is a healthy reason.

### ✅ Stage 2 Checkpoint *(closed-book, 3 min)*
**Q:** A company's Accounts Receivable rises by \$40M in a year. What happens to Operating Cash Flow relative to Net Income, and why?
<details>
<summary>Show answer</summary>

Operating Cash Flow is lower by \$40M relative to Net Income. Revenue was recorded, but customers have not paid yet, so cash did not arrive.

</details>

### 🧪 Next: Lab 2 `[MVW]`
> 👉 **Do now:** [Lab 2 — Cash vs Profit Teardown](Week-01-Practice.md#lab-2) (~25 min)
> **What this lab proves:** you can find Net Income, OCF, and FCF in a real 10-K and explain the gap.
> **Done when:** you wrote 3 bullets and named at least 1 concrete driver. **Short on time this week? This is the one lab to do.** Then continue to Stage 3.

---

<a id="stage-3"></a>
## Stage 3 — Working capital warning signs
> **Stage goal:** you can spot when growth is consuming cash instead of producing it.

- **Why it matters:** many failing companies show rising revenue and profit while cash drains away.
- **Analogy from your background:** like a service whose request backlog (receivables, inventory) grows faster than its throughput. Latency hides until the queue overflows.
- **How it works:** working capital = current assets − current liabilities. Watch three lines:

| Line | Warning sign | Follow-up number |
| :--- | :--- | :--- |
| Accounts Receivable | Grows faster than revenue | Days Sales Outstanding (DSO) |
| Inventory | Grows faster than sales | Days Inventory Outstanding |
| Accounts Payable | Stretching suppliers to hide cash stress | Days Payables Outstanding |

- **Worked example:** revenue +40% but receivables +100%. Customers are paying more slowly, or revenue is being booked on loose terms. Check DSO trend and the share of revenue from the top customers.
- **Watch out:** one bad quarter is noise. Look for a trend over at least 3–4 periods.

### ✅ Stage 3 Checkpoint *(closed-book, 3 min)*
**Q:** Revenue grows 40% and OCF turns negative. Name 2 numbers you would check next.
<details>
<summary>Show answer</summary>

For example: DSO (or receivables as a share of revenue) over several periods, and the cash balance versus the year's cash burn, which tells you how many months of runway remain. Customer concentration and the allowance for doubtful accounts are also valid.

</details>

### 🧪 Next: Lab 3
> 👉 **Do now:** [Lab 3 — Profitable but Dying Trap](Week-01-Practice.md#lab-3) (~30 min)
> **What this lab proves:** you can turn three symptoms into a hypothesis and two follow-up checks.
> **Done when:** your 5-line diagnosis names an operational cause and 2 numbers to verify. Then continue to Stage 4.

---

<a id="stage-4"></a>
## Stage 4 — Integrate: the Health Snapshot
> **Stage goal:** you can combine the three statements into a short, evidence-based judgment.

- **No new theory.** Use a three-question frame:
  1. **Does it generate cash?** Operating Cash Flow and FCF over 2–3 years.
  2. **Is the balance sheet resilient?** Net Cash = Cash + Short-term Investments − Total Debt. Does FCF cover interest, dividends, and buybacks?
  3. **What is the main risk?** One specific number, for example a receivables spike or rising debt.
- **Format:** 150 words, at least 3 numbers, drawn from at least 2 statements.

### 🧪 Next: Lab 4 — Transfer Challenge
> 👉 **Do now:** [Lab 4 — Transfer Challenge](Week-01-Practice.md#lab-4) (~45 min)
> **What this lab proves:** you can do the whole workflow unaided on a company you choose.
> **Done when:** you scored yourself on the rubric and ran the AI Critique Prompt. Then do the Active Recall Check below.

---

## Common Pitfalls & Key Takeaways
1. **Pitfall:** treating Net Income as cash. → **Instead:** always put OCF next to it.
2. **Pitfall:** reading one year. → **Instead:** compare at least 2–3 years to see the trend.
3. **Pitfall:** calling every gap between profit and cash a red flag. → **Instead:** identify the driver first (deferred revenue vs receivables).

## Active Recall Check *(Closed-Book, after all Labs)*

**Q1:** Which statement is a point-in-time snapshot, and which two cover a period?
<details>
<summary>Show answer</summary>

The Balance Sheet is a snapshot. The Income Statement and Cash Flow Statement cover a period.

</details>

**Q2:** Write the formula for Free Cash Flow.
<details>
<summary>Show answer</summary>

FCF = Operating Cash Flow − Capital Expenditures.

</details>

**Q3:** A company collects \$60,000 upfront for a 6-month service starting this month. How much revenue does it recognize this month?
<details>
<summary>Show answer</summary>

\$10,000 (\$60,000 ÷ 6). The other \$50,000 sits in Deferred Revenue.

</details>

**Q4:** Give one reason OCF can exceed Net Income.
<details>
<summary>Show answer</summary>

Non-cash expenses such as depreciation or stock-based compensation, or growth in deferred revenue.

</details>

**Q5:** What is Net Cash, and why does it matter in a downturn?
<details>
<summary>Show answer</summary>

Net Cash = Cash + Short-term Investments − Total Debt. A positive figure means the company could repay its debt from liquid assets, so it can survive a revenue drop longer.

</details>
