# Is Palindrome — Solution Explanation

## Problem

Given a string `s`, determine if it is a palindrome after converting to lowercase
and removing all non-alphanumeric characters.

**Example**: `"A man, a plan, a canal: Panama"` → cleaned: `"amanaplanacanalpanama"` → **True**

## Key Insight

Instead of creating a cleaned copy of the string (extra space), use **two pointers** —
one at the start, one at the end — and skip non-alphanumeric characters in-place.
Compare characters in lowercase as the pointers move inward.

## Approach: Two Pointers

### Data Structures Used
- **Two index variables**: `left` (start) and `right` (end) — no extra data structures needed.

### Step-by-Step Logic

1. **Initialise** `left = 0` and `right = len(s) - 1`.
2. **While** `left < right`:
   - **Skip non-alphanumeric** characters on the left by incrementing `left`.
   - **Skip non-alphanumeric** characters on the right by decrementing `right`.
   - **Compare** `s[left].lower()` with `s[right].lower()`.
     - If they differ → return `False`.
   - **Move** both pointers inward: `left += 1`, `right -= 1`.
3. If the loop completes, all pairs matched → return `True`.

### Walkthrough

```
Input: "A man, a plan, a canal: Panama"

left=0 ('A'), right=29 ('a')  → 'a' == 'a' ✓ → move inward
left=1 (' '), skip → left=2 ('m')
right=28 ('m')                 → 'm' == 'm' ✓ → move inward
left=3 ('a'), right=27 ('a')  → 'a' == 'a' ✓ → move inward
... continues matching until pointers cross ...

Output: True
```

## Edge Cases
- **Empty string** `""` → pointers never enter loop → `True`.
- **All non-alphanumeric** `".,!?  "` → pointers skip everything → `True`.
- **Single character** `"a"` → `True`.

## Complexity
- **Time**: O(n) — each character visited at most once.
- **Space**: O(1) — no extra data structures, just two pointers.
