# Three Integer Sum — Solution Explanation

## Problem

Given an integer array `nums`, return all **unique triplets** `[nums[i], nums[j], nums[k]]`
such that `i ≠ j ≠ k` and `nums[i] + nums[j] + nums[k] == 0`.
The solution set must not contain duplicate triplets.

**Example**: `[-1, 0, 1, 2, -1, -4]` → `[[-1, -1, 2], [-1, 0, 1]]`

## Key Insight

**Sort the array first.** Then for each element, the problem reduces to **Two Sum** on the
remaining subarray — solvable with two pointers. Sorting also makes it easy to **skip duplicates**.

## Approach: Sort + Two Pointers

### Data Structures Used
- **Sorted array**: Enables two-pointer technique and duplicate skipping.
- **Result list**: Collects valid triplets.

### Step-by-Step Logic

1. **Sort** `nums` in ascending order.
2. **Iterate** `i` from 0 to end:
   - **Early exit**: if `nums[i] > 0`, no triplet can sum to 0 (all remaining are positive) → break.
   - **Skip duplicates**: if `nums[i] == nums[i-1]`, skip to avoid duplicate triplets.
   - Set `l = i + 1`, `r = len(nums) - 1` (two pointers on remaining subarray).
   - **While** `l < r`:
     - Compute `three_sum = nums[i] + nums[l] + nums[r]`.
     - If `three_sum > 0`: sum too large → `r -= 1`.
     - If `three_sum < 0`: sum too small → `l += 1`.
     - If `three_sum == 0`: found a valid triplet!
       - Append `[nums[i], nums[l], nums[r]]` to result.
       - Move both pointers inward, and skip duplicate values of `nums[l]`.
3. **Return** result.

### Walkthrough

```
nums = [-1, 0, 1, 2, -1, -4]
sorted = [-4, -1, -1, 0, 1, 2]

i=0, nums[i]=-4:
  l=1(-1), r=5(2): sum=-4-1+2=-3 < 0 → l++
  l=2(-1), r=5(2): sum=-4-1+2=-3 < 0 → l++
  l=3(0),  r=5(2): sum=-4+0+2=-2 < 0 → l++
  l=4(1),  r=5(2): sum=-4+1+2=-1 < 0 → l++
  l=5 → l >= r, stop

i=1, nums[i]=-1:
  l=2(-1), r=5(2): sum=-1-1+2=0 ✓ → add [-1,-1,2], l++, r--
  l=3(0),  r=4(1): sum=-1+0+1=0 ✓ → add [-1,0,1], l++, r--
  l=4 → l >= r, stop

i=2, nums[i]=-1: same as nums[1] → skip (duplicate)

i=3, nums[i]=0: 0 is not > 0
  l=4(1), r=5(2): sum=0+1+2=3 > 0 → r--
  l=4 → l >= r, stop

i=4, nums[i]=1: 1 > 0 → break

Output: [[-1,-1,2], [-1,0,1]]
```

## Edge Cases
- **Fewer than 3 elements** → no triplets possible.
- **All zeros** `[0, 0, 0]` → `[[0, 0, 0]]`.
- **No valid triplets** `[1, 2, 3]` → `[]`.

## Complexity
- **Time**: O(n²) — outer loop O(n) × inner two-pointer O(n).
- **Space**: O(1) extra (ignoring output and sort space).
