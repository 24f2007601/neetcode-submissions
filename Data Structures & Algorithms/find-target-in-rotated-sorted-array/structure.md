# Find Target in Rotated Sorted Array — Solution Explanation

## Problem

Given a sorted array `nums` of unique integers that has been rotated, and a `target` value,
return the **index** of `target` if it exists, otherwise return `-1`. You must solve it in O(log n) time.

**Example**: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0` → `4`

## Key Insight

A rotated sorted array always has **one fully sorted half**. At each step of binary search,
identify which half is sorted, then check if `target` falls within that sorted range.
This lets you eliminate half the array each iteration — just like standard binary search.

## Approach: Modified Binary Search

### Data Structures Used
- **Two pointers** (`left`, `right`): define the binary search window.

### Step-by-Step Logic

1. **Initialise** `left = 0`, `right = len(nums) - 1`.
2. **While** `left <= right`:
   - Compute `mid = (left + right) // 2`.
   - **If** `nums[mid] == target`: return `mid` (found!).
   - **Determine which half is sorted**:
     - **If** `nums[left] <= nums[mid]` → the **left half** `[left..mid]` is sorted:
       - If `nums[left] <= target < nums[mid]` → target is in the left half → `right = mid - 1`.
       - Else → target is in the right half → `left = mid + 1`.
     - **Else** → the **right half** `[mid..right]` is sorted:
       - If `nums[mid] <= target <= nums[right]` → target is in the right half → `left = mid + 1`.
       - Else → target is in the left half → `right = mid - 1`.
3. **Return** `-1` — target was not found.

### Walkthrough

```
nums = [4, 5, 6, 7, 0, 1, 2], target = 0

left=0, right=6, mid=3:  nums[3]=7 ≠ 0
  nums[0]=4 ≤ nums[3]=7 → left half sorted
  4 ≤ 0 < 7? No → left=4

left=4, right=6, mid=5:  nums[5]=1 ≠ 0
  nums[4]=0 ≤ nums[5]=1 → left half sorted
  0 ≤ 0 < 1? Yes → right=4

left=4, right=4, mid=4:  nums[4]=0 == 0 → return 4 ✓
```

### Why Checking the Sorted Half Works

- In a rotated array, exactly one half around `mid` is always fully sorted.
- A sorted range has a known min and max, so we can check if `target` falls within it
  using simple comparisons.
- This preserves the O(log n) halving property of binary search.

## Edge Cases
- **Not rotated** `[1, 2, 3, 4, 5]`, target `3` → `2` (standard binary search).
- **Single element** `[1]`, target `1` → `0`.
- **Target not present** `[4, 5, 6, 7, 0, 1, 2]`, target `3` → `-1`.
- **Target at rotation point** `[4, 5, 6, 7, 0, 1, 2]`, target `0` → `4`.

## Complexity
- **Time**: O(log n) — binary search halving at every step.
- **Space**: O(1) — only pointer variables.
