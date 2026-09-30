# Buy and Sell Crypto — Solution Explanation

## Problem

Given a list of daily prices, find the maximum profit from a single buy-sell transaction.
You must buy before you sell — you cannot sell on a day before you buy.

**Example**: `[7, 1, 5, 3, 6, 4]` → Buy at 1, sell at 6 → Profit = **5**

## Key Insight

We only need to track the **lowest price seen so far** as we scan left-to-right.
At each day, the best we can do is sell at today's price minus that lowest past price.
This turns a seemingly O(n²) problem into a single-pass O(n) solution.

## Approach: Single Pass with Running Minimum

### Data Structures Used
- **Two variables**: `min_price` (lowest price seen so far) and `max_profit` (best profit found so far).

### Step-by-Step Logic

1. **Initialise** `min_price = infinity` and `max_profit = 0`.
2. **Iterate** through each `price` in the list:
   - If `price < min_price`: we found a new cheapest buy day → update `min_price`.
   - Otherwise, calculate `price - min_price` (profit if we sold today).
     If this beats `max_profit`, update `max_profit`.
3. **Return** `max_profit`.

### Walkthrough

```
prices = [7, 1, 5, 3, 6, 4]

Day 0: price=7  → min_price=7, max_profit=0
Day 1: price=1  → min_price=1, max_profit=0        (new low found)
Day 2: price=5  → profit=5-1=4 → max_profit=4
Day 3: price=3  → profit=3-1=2 → max_profit=4      (no improvement)
Day 4: price=6  → profit=6-1=5 → max_profit=5      ← best
Day 5: price=4  → profit=4-1=3 → max_profit=5      (no improvement)

Output: 5
```

## Edge Cases
- **Prices always decrease** `[7, 6, 4, 3, 1]` → no profitable trade → return 0.
- **Single price** → no trade possible → return 0.
- **All same prices** `[3, 3, 3]` → profit is 0.

## Complexity
- **Time**: O(n) — single pass.
- **Space**: O(1) — only two variables.
