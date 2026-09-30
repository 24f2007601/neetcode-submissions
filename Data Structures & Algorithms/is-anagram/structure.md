# Is Anagram — Solution Explanation

## Problem

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.
An anagram uses the exact same characters with the exact same frequencies, just rearranged.

**Example**: `s = "anagram"`, `t = "nagaram"` → `True`

## Key Insight

If two strings are anagrams, sorting them both produces the **exact same sequence of characters**.
This is the simplest way to check — just compare sorted versions.

## Approach: Sort and Compare

### Step-by-Step Logic

1. **Sort** all characters of `s` into a list.
2. **Sort** all characters of `t` into a list.
3. **Compare** the two sorted lists — if equal, the strings are anagrams.

### Walkthrough

```
s = "anagram", t = "nagaram"

sorted("anagram") = ['a', 'a', 'a', 'g', 'm', 'n', 'r']
sorted("nagaram") = ['a', 'a', 'a', 'g', 'm', 'n', 'r']

They match → return True ✓
```

## Alternative Approach
- **Frequency counting** with `Counter(s) == Counter(t)` gives O(n) time but this
  sorting approach is simpler and perfectly adequate for interview purposes.

## Edge Cases
- **Different lengths** → `sorted` will produce different-length lists → `False`.
- **Empty strings** `"", ""` → both sort to `[]` → `True`.
- **Single characters** `"a", "b"` → `['a'] != ['b']` → `False`.

## Complexity
- **Time**: O(n log n) — dominated by sorting.
- **Space**: O(n) — sorted copies of both strings.
