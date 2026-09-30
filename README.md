# NeetCode Solutions — @24f2007601

> Synced automatically from [NeetCode.io](https://neetcode.io) · Repository: `neetcode-submissions`

---

## What is this?

[NeetCode.io](https://neetcode.io) is a coding interview preparation platform featuring curated problems, video solutions, and an in-browser code editor. This repository is automatically populated with your accepted (or all) solutions using the **GitHub Sync** feature.

Each solution folder includes a **`structure.md`** file that breaks down the logic of the program into simple, detailed steps — including the key insight, step-by-step walkthrough, edge cases, and time/space complexity.

---

## How GitHub Sync works

1. **Connect your GitHub account** on [neetcode.io/profile/github](https://neetcode.io/profile/github).
2. **Auto-commit** — every time you submit a solution on NeetCode, it is pushed here automatically (configurable by status).
3. **Bulk Sync** — push all your past solutions at once from the GitHub settings page.
4. **Manual sync** — from the submission history panel on any problem page, sync or remove individual submissions.

---

## Repository structure

Solutions are organized by topic folder, then problem ID. Each submission is stored as a separate file, accompanied by an explanation:

```
<topic-folder>/
  <problem-id>/
    submission-0.<ext>   ← solution code (with inline comments)
    structure.md         ← detailed logic explanation
```

**Example:**
```
Data Structures & Algorithms/two-integer-sum/submission-0.py
Data Structures & Algorithms/two-integer-sum/structure.md
```

---

## Problems Solved

### Data Structures & Algorithms

| # | Problem | Approach | Complexity | Files |
|---|---------|----------|------------|-------|
| 1 | **Two Integer Sum** | One-pass hash map (complement lookup) | O(n) / O(n) | [solution](Data%20Structures%20%26%20Algorithms/two-integer-sum/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/two-integer-sum/structure.md) |
| 2 | **Duplicate Integer** | Hash set (track seen numbers) | O(n) / O(n) | [solution](Data%20Structures%20%26%20Algorithms/duplicate-integer/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/duplicate-integer/structure.md) |
| 3 | **Is Anagram** | Sort and compare | O(n log n) / O(n) | [solution](Data%20Structures%20%26%20Algorithms/is-anagram/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/is-anagram/structure.md) |
| 4 | **Anagram Groups** | Hash map with sorted-character key | O(N·K log K) / O(NK) | [solution](Data%20Structures%20%26%20Algorithms/anagram-groups/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/anagram-groups/structure.md) |
| 5 | **Top K Elements in List** | Frequency map + bucket sort | O(n) / O(n) | [solution](Data%20Structures%20%26%20Algorithms/top-k-elements-in-list/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/top-k-elements-in-list/structure.md) |
| 6 | **String Encode and Decode** | Length-prefix protocol | O(n) / O(n) | [solution](Data%20Structures%20%26%20Algorithms/string-encode-and-decode/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/string-encode-and-decode/structure.md) |
| 7 | **Concatenation of Array** | Direct list concatenation | O(n) / O(n) | [solution](Data%20Structures%20%26%20Algorithms/concatenation-of-array/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/concatenation-of-array/structure.md) |
| 8 | **Products of Array Discluding Self** | Prefix + suffix product passes | O(n) / O(1) | [solution](Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self/structure.md) |
| 9 | **Valid Sudoku** | Three arrays of sets (row, col, box) | O(1) / O(1) | [solution](Data%20Structures%20%26%20Algorithms/valid-sudoku/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/valid-sudoku/structure.md) |
| 10 | **Is Palindrome** | Two pointers (skip non-alnum, compare) | O(n) / O(1) | [solution](Data%20Structures%20%26%20Algorithms/is-palindrome/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/is-palindrome/structure.md) |
| 11 | **Three Integer Sum** | Sort + two pointers | O(n²) / O(1) | [solution](Data%20Structures%20%26%20Algorithms/three-integer-sum/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/three-integer-sum/structure.md) |
| 12 | **Max Water Container** | Two pointers (greedy, move shorter side) | O(n) / O(1) | [solution](Data%20Structures%20%26%20Algorithms/max-water-container/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/max-water-container/structure.md) |
| 13 | **Buy and Sell Crypto** | Single pass with running minimum | O(n) / O(1) | [solution](Data%20Structures%20%26%20Algorithms/buy-and-sell-crypto/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/buy-and-sell-crypto/structure.md) |
| 14 | **Longest Substring Without Duplicates** | Sliding window + hash set | O(n) / O(n) | [solution](Data%20Structures%20%26%20Algorithms/longest-substring-without-duplicates/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/longest-substring-without-duplicates/structure.md) |
| 15 | **Longest Repeating Substring with Replacement** | Sliding window + frequency map | O(n) / O(1) | [solution](Data%20Structures%20%26%20Algorithms/longest-repeating-substring-with-replacement/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/longest-repeating-substring-with-replacement/structure.md) |
| 16 | **Validate Parentheses** | Stack with bracket mapping | O(n) / O(n) | [solution](Data%20Structures%20%26%20Algorithms/validate-parentheses/submission-0.py) · [explanation](Data%20Structures%20%26%20Algorithms/validate-parentheses/structure.md) |

> **Complexity** is listed as Time / Space.

---

## What's in each `structure.md`?

Every explanation file follows a consistent format:

- **Problem** — statement with example
- **Key Insight** — the core idea that makes the solution work
- **Approach** — named technique and data structures used
- **Step-by-Step Logic** — detailed numbered walkthrough of the algorithm
- **Walkthrough** — traced example with intermediate state
- **Edge Cases** — inputs to watch out for
- **Complexity** — time and space analysis

---

## Supported languages

| Language | Extension |
|---|---|
| Python | `.py` |
| JavaScript | `.js` |
| TypeScript | `.ts` |
| Java | `.java` |
| C++ | `.cpp` |
| C# | `.cs` |
| Go | `.go` |
| Rust | `.rs` |
| Kotlin | `.kt` |
| Swift | `.swift` |
| SQL | `.sql` |

---

## Settings

Manage your sync preferences at [neetcode.io/profile/github](https://neetcode.io/profile/github):

- **Auto-commit toggle** — enable or disable automatic commits on submission
- **Status filter** — sync all submissions or accepted only
- **Rename repository** — rename this repo or start fresh with a new one
- **Bulk Sync** — push all past solutions at once (rate-limited)

---

*Generated by [NeetCode GitHub Integration](https://neetcode.io)*
