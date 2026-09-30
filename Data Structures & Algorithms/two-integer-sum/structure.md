# Two Integer Sum — Solution Explanation

## Problem

Given an array `nums` and a `target`, return the **indices** of the two numbers
that add up to `target`. Each input has exactly one solution.

**Example**: `nums = [2, 7, 11, 15]`, `target = 9` → `[0, 1]` (because 2 + 7 = 9)

## Key Insight

For each number, we need to find if its **complement** (`target - num`) exists earlier
in the array. A **hash map** gives O(1) lookups, turning a brute-force O(n²) approach into O(n).

## Approach: One-Pass Hash Map

### Data Structures Used
- **`num_map` dict**: Maps each number to its index — enables O(1) complement lookups.

### Step-by-Step Logic

1. **Create** an empty dictionary `num_map`.
2. **Iterate** through the array with `enumerate` to get both index `i` and value `num`:
   - Compute `complement = target - num`.
   - **If** `complement` exists in `num_map`, we found the pair!
     → Return `[num_map[complement], i]`.
   - **Otherwise**, store `num_map[num] = i` for future lookups.
3. The problem guarantees exactly one solution, so the loop always finds a pair.

### Walkthrough

```
nums = [2, 7, 11, 15], target = 9

i=0, num=2:  complement=9-2=7,  7 not in {} → store {2:0}
i=1, num=7:  complement=9-7=2,  2 IS in {2:0} → return [0, 1] ✓
```

### Why One-Pass Works

We check for the complement **before** inserting the current number. This means:
- We never match a number with itself.
- We always find the pair on the second number's iteration.

## Edge Cases
- **Negative numbers** `[-1, -2, -3, -4, -5]`, target = `-8` → works the same.
- **Zero in array** `[0, 4, 3, 0]`, target = `0` → `[0, 3]`.
- **Two elements** `[3, 3]`, target = `6` → `[0, 1]`.

## Complexity
- **Time**: O(n) — single pass with O(1) hash map operations.
- **Space**: O(n) — storing up to n entries in the map.
