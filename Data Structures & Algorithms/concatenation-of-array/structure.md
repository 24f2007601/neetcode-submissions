# Concatenation of Array — Solution Explanation

## Problem

Given an integer array `nums` of length `n`, return an array of length `2n` where
`ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n`.
In other words, concatenate the array with itself.

**Example**: `[1, 2, 1]` → `[1, 2, 1, 1, 2, 1]`

## Key Insight

Python's `+` operator on lists already performs concatenation.
`nums + nums` creates a new list that is the original array repeated twice.

## Approach: Direct Concatenation

### Step-by-Step Logic

1. **Return** `nums + nums` — Python concatenates the two lists into one.

### Walkthrough

```
Input:  [1, 2, 1]
nums + nums = [1, 2, 1] + [1, 2, 1] = [1, 2, 1, 1, 2, 1]
Output: [1, 2, 1, 1, 2, 1]
```

## Edge Cases
- **Single element** `[1]` → `[1, 1]`.
- **Empty array** `[]` → `[]`.

## Complexity
- **Time**: O(n) — copying n elements twice.
- **Space**: O(n) — the new list of size 2n.
