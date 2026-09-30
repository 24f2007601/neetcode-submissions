# Products of Array Discluding Self — Solution Explanation

## Problem

Given an integer array `nums`, return an array `output` where `output[i]` equals the
product of all elements in `nums` **except** `nums[i]`. Solve it **without division**.

**Example**: `[1, 2, 3, 4]` → `[24, 12, 8, 6]`

## Key Insight

For each position `i`, the answer is `(product of everything to the left) × (product of everything to the right)`.
We can compute left-products (prefix) and right-products (suffix) in two separate passes,
storing the result directly in the output array — no division needed.

## Approach: Prefix and Suffix Products

### Data Structures Used
- **`output` array**: Initialised to all 1s; used to accumulate both prefix and suffix products.
- **Two variables**: `prefix` and `suffix` — running products.

### Step-by-Step Logic

1. **Create** `output = [1, 1, ..., 1]` of the same length as `nums`.
2. **Prefix pass** (left → right):
   - Maintain `prefix = 1`.
   - For each index `i`: set `output[i] = prefix`, then multiply `prefix *= nums[i]`.
   - After this pass, `output[i]` = product of all elements **before** index `i`.
3. **Suffix pass** (right → left):
   - Maintain `suffix = 1`.
   - For each index `i` (from end to start): multiply `output[i] *= suffix`, then multiply `suffix *= nums[i]`.
   - After this pass, `output[i]` = (product before `i`) × (product after `i`).
4. **Return** `output`.

### Walkthrough

```
nums = [1, 2, 3, 4]

Prefix pass (left → right):
  i=0: output[0]=1,    prefix=1×1=1
  i=1: output[1]=1,    prefix=1×2=2
  i=2: output[2]=2,    prefix=2×3=6
  i=3: output[3]=6,    prefix=6×4=24
  output = [1, 1, 2, 6]  ← each cell = product of elements to its LEFT

Suffix pass (right → left):
  i=3: output[3]=6×1=6,   suffix=1×4=4
  i=2: output[2]=2×4=8,   suffix=4×3=12
  i=1: output[1]=1×12=12, suffix=12×2=24
  i=0: output[0]=1×24=24, suffix=24×1=24
  output = [24, 12, 8, 6]  ← each cell = LEFT product × RIGHT product

Output: [24, 12, 8, 6] ✓
```

## Edge Cases
- **Contains a zero** `[0, 1, 2]` → `[2, 0, 0]` — handled naturally.
- **Two elements** `[3, 5]` → `[5, 3]`.
- **All ones** `[1, 1, 1]` → `[1, 1, 1]`.

## Complexity
- **Time**: O(n) — two linear passes.
- **Space**: O(1) extra — output array is the answer, not extra space.
