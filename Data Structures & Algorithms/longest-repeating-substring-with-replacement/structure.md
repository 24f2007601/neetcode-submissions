# Longest Repeating Substring with Replacement — Solution Explanation

## Problem

Given a string `s` and an integer `k`, find the length of the longest substring where
you can replace **at most `k`** characters to make every character in the substring the same.

**Example**: `s = "AABABBA"`, `k = 1` → `"AABAB"` → replace one B → `"AAAAB"` is invalid, 
but `"ABAB"` → replace 1 → `"AAAA"` length 4 → **Output: 4**

## Key Insight

In any window of size `W`, if the **most frequent character** appears `max_freq` times,
then we need to replace `W - max_freq` characters to make all characters the same.
If `W - max_freq <= k`, the window is valid. This gives us a **sliding window** approach.

## Approach: Sliding Window with Frequency Map

### Data Structures Used
- **`count` dict**: Frequency of each character in the current window.
- **`max_freq`**: The highest frequency of any single character in the current window.
- **`left`, `right`**: Sliding window boundaries.

### Step-by-Step Logic

1. **Initialise** `count = {}`, `max_freq = 0`, `max_len = 0`, `left = 0`.
2. **Expand** the window by moving `right` from 0 to end:
   - Increment `count[s[right]]`.
   - Update `max_freq = max(max_freq, count[s[right]])`.
   - **Check validity**: if `(window size) - max_freq > k`, the window has too many characters
     to replace — **shrink** by decrementing `count[s[left]]` and moving `left` forward.
   - Update `max_len` with the current window size.
3. **Return** `max_len`.

### Why We Don't Decrease `max_freq`

When we shrink the window, we don't decrease `max_freq` because a smaller `max_freq`
can never produce a longer valid window than what we've already found. This is a safe
optimisation that keeps the algorithm O(n).

### Walkthrough

```
s = "AABABBA", k = 1

right=0: 'A' count={'A':1}      max_freq=1 window=1 valid(1-1=0≤1) max_len=1
right=1: 'A' count={'A':2}      max_freq=2 window=2 valid(2-2=0≤1) max_len=2
right=2: 'B' count={'A':2,'B':1} max_freq=2 window=3 valid(3-2=1≤1) max_len=3
right=3: 'A' count={'A':3,'B':1} max_freq=3 window=4 valid(4-3=1≤1) max_len=4
right=4: 'B' count={'A':3,'B':2} max_freq=3 window=5 invalid(5-3=2>1) → shrink left
         count={'A':2,'B':2} left=1, window=4 max_len=4
right=5: 'B' count={'A':2,'B':3} max_freq=3 window=5 invalid(5-3=2>1) → shrink
         count={'A':1,'B':3} left=2, window=4 max_len=4
right=6: 'A' count={'A':2,'B':3} max_freq=3 window=5 invalid(5-3=2>1) → shrink
         count={'A':2,'B':2} left=3, window=4 max_len=4

Output: 4
```

## Edge Cases
- **k >= len(s)** → can replace everything → answer is `len(s)`.
- **All same characters** `"AAAA"` → answer is `len(s)` regardless of k.
- **k = 0** → longest run of a single repeated character.

## Complexity
- **Time**: O(n) — each character is added/removed from the window at most once.
- **Space**: O(1) — at most 26 entries in the frequency map.
