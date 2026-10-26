# Find Minimum in Rotated Sorted Array — Solution Explanation

## Problem

Given a sorted array `nums` of unique integers that has been rotated between 1 and n times,
find the **minimum** element. You must solve it in O(log n) time.

**Example**: `nums = [3, 4, 5, 1, 2]` → `1`

## Key Insight

A rotated sorted array has two sorted halves. The minimum element sits at the **rotation pivot** —
the boundary between the higher left half and the lower right half. Binary search can find this
pivot by comparing `nums[mid]` against `nums[right]`.

## Approach: Modified Binary Search

### Data Structures Used
- **Two pointers** (`left`, `right`): define the binary search window.

### Step-by-Step Logic

1. **Initialise** `left = 0`, `right = len(nums) - 1`.
2. **While** `left < right`:
   - Compute `mid = left + (right - left) // 2`.
   - **If** `nums[mid] > nums[right]`: the pivot (minimum) must be to the right of `mid`
     → set `left = mid + 1`.
   - **Else**: `mid` could be the minimum, or it's to the left
     → set `right = mid`.
3. **Return** `nums[left]` — `left == right`, converged on the minimum.

### Walkthrough

```
nums = [3, 4, 5, 1, 2]

left=0, right=4, mid=2:  nums[2]=5 > nums[4]=2 → left=3
left=3, right=4, mid=3:  nums[3]=1 ≤ nums[4]=2 → right=3
left=3, right=3 → return nums[3] = 1 ✓
```

### Why `nums[mid] > nums[right]` Works

- If `nums[mid] > nums[right]`, the array is "broken" between `mid` and `right`,
  so the minimum is in `[mid+1, right]`.
- Otherwise, the minimum is in `[left, mid]` (inclusive — `mid` itself could be it).

## Edge Cases
- **Not rotated** `[1, 2, 3, 4, 5]` → `1` (left pointer stays at 0).
- **Single element** `[1]` → `1` (loop never executes).
- **Two elements** `[2, 1]` → `1`.

## Complexity
- **Time**: O(log n) — standard binary search halving.
- **Space**: O(1) — only two pointer variables.
