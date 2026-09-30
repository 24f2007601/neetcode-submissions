# Top K Elements in List — Solution Explanation

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

**Example**: `nums = [1,1,1,2,2,3]`, `k = 2` → `[1, 2]`

## Key Insight

Instead of sorting by frequency (O(n log n)), use **bucket sort**. Create an array of
buckets where index = frequency. Since no element can appear more than `n` times,
we only need `n + 1` buckets. Then scan from the highest bucket downward to collect
the top-k elements in O(n) time.

## Approach: Frequency Map + Bucket Sort

### Data Structures Used
- **`count` dict**: Maps each number to its frequency.
- **`buckets` list**: Index `i` holds a list of numbers that appear exactly `i` times.

### Step-by-Step Logic

1. **Count frequencies**: Build a hashmap `count` where `count[num]` = how many times `num` appears.
2. **Fill buckets**: Create `len(nums) + 1` empty buckets. For each `(num, freq)` pair, append `num` to `buckets[freq]`.
3. **Collect top-k**: Iterate from the highest bucket index down to 1.
   - For each number in the current bucket, append it to `result`.
   - As soon as `result` has `k` elements, return immediately.

### Walkthrough

```
nums = [1, 1, 1, 2, 2, 3], k = 2

Step 1 — Count: {1: 3, 2: 2, 3: 1}

Step 2 — Buckets (index = frequency):
  buckets[0] = []
  buckets[1] = [3]       ← 3 appears 1 time
  buckets[2] = [2]       ← 2 appears 2 times
  buckets[3] = [1]       ← 1 appears 3 times
  buckets[4] = []
  buckets[5] = []
  buckets[6] = []

Step 3 — Collect from highest bucket:
  i=6: empty
  i=5: empty
  i=4: empty
  i=3: [1] → result = [1]  (need 1 more)
  i=2: [2] → result = [1, 2]  (k=2 reached!) → return

Output: [1, 2]
```

## Edge Cases
- **k equals number of unique elements** → return all unique elements.
- **All elements the same** `[5, 5, 5]`, `k = 1` → `[5]`.
- **k = 1** → return the single most frequent element.

## Complexity
- **Time**: O(n) — counting is O(n), bucket creation is O(n), collection is O(n) worst case.
- **Space**: O(n) — for the frequency map and bucket array.
