# Duplicate Integer — Solution Explanation

## Problem

Given an integer array `nums`, return `True` if any value appears **at least twice**,
and `False` if every element is distinct.

**Example**: `[1, 2, 3, 1]` → `True` (1 appears twice)

## Key Insight

A **set** provides O(1) average-case lookup. As we scan the array, we can check
whether we've already seen a number before adding it. The first repeat ends the search early.

## Approach: Hash Set

### Data Structures Used
- **`set`**: Stores numbers we've encountered so far. Set membership check is O(1) average.

### Step-by-Step Logic

1. **Create** an empty set `seen`.
2. **Iterate** through each `num` in the array:
   - If `num` is already in `seen`, we found a duplicate → return `True`.
   - Otherwise, **add** `num` to `seen`.
3. If the loop finishes without finding a duplicate, return `False`.

### Walkthrough

```
Input: [1, 2, 3, 1]

num=1 → seen={},    1 not in seen → add → seen={1}
num=2 → seen={1},   2 not in seen → add → seen={1,2}
num=3 → seen={1,2}, 3 not in seen → add → seen={1,2,3}
num=1 → seen={1,2,3}, 1 IS in seen → return True ✓
```

## Edge Cases
- **Empty array** `[]` → no duplicates → `False`.
- **Single element** `[5]` → `False`.
- **All identical** `[2, 2, 2]` → `True` on second element.

## Complexity
- **Time**: O(n) — single pass; set operations are O(1) average.
- **Space**: O(n) — worst case stores all n elements in the set.
