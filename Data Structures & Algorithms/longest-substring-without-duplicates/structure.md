# Longest Substring Without Duplicates — Solution Explanation

## Problem

Given a string `s`, find the length of the **longest substring** that contains
no repeating characters.

**Example**: `"abcabcbb"` → `"abc"` → length **3**

## Key Insight

Use a **sliding window** with a **set** to track characters in the current window.
When a duplicate is detected, shrink the window from the left until the duplicate
is removed. This ensures every window is always valid (no repeats).

## Approach: Sliding Window with Hash Set

### Data Structures Used
- **`char_set` (set)**: Characters currently in the window — O(1) lookup.
- **`left`**: Left boundary of the window.

### Step-by-Step Logic

1. **Initialise** `char_set = set()`, `left = 0`, `max_length = 0`.
2. **Expand** the window by moving `right` from 0 to end:
   - **While** `s[right]` is already in `char_set` (duplicate detected):
     - Remove `s[left]` from the set and increment `left` (shrink window).
   - **Add** `s[right]` to the set.
   - **Update** `max_length = max(max_length, right - left + 1)`.
3. **Return** `max_length`.

### Walkthrough

```
Input: "abcabcbb"

right=0 'a': set={a}         window="a"     max_length=1
right=1 'b': set={a,b}       window="ab"    max_length=2
right=2 'c': set={a,b,c}     window="abc"   max_length=3
right=3 'a': 'a' in set! → remove 'a', left=1 → set={b,c}
             add 'a' → set={b,c,a}  window="bca"  max_length=3
right=4 'b': 'b' in set! → remove 'b', left=2 → set={c,a}
             add 'b' → set={c,a,b}  window="cab"  max_length=3
right=5 'c': 'c' in set! → remove 'c', left=3 → set={a,b}
             add 'c' → set={a,b,c}  window="abc"  max_length=3
right=6 'b': 'b' in set! → remove 'a', left=4 → still 'b' in set
             → remove 'b', left=5 → set={c}
             add 'b' → set={c,b}  window="cb"  max_length=3
right=7 'b': 'b' in set! → remove 'c', left=6 → still 'b' in set
             → remove 'b', left=7 → set={}
             add 'b' → set={b}  window="b"  max_length=3

Output: 3
```

## Note on Submissions
- **submission-0.py** and **submission-1.py** contain identical code (same approach).

## Edge Cases
- **Empty string** `""` → `max_length` stays 0.
- **All unique** `"abcde"` → window grows to full length → answer is `len(s)`.
- **All same** `"aaaaa"` → window is always size 1.

## Complexity
- **Time**: O(n) — each character is added and removed from the set at most once.
- **Space**: O(min(n, alphabet_size)) — set stores at most the number of unique characters.
