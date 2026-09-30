# Max Water Container — Solution Explanation

## Problem

Given an array `heights` where `heights[i]` is the height of a vertical line at position `i`,
find two lines that together with the x-axis form a container holding the most water.

**Example**: `[1,8,6,2,5,4,8,3,7]` → lines at index 1 (h=8) and index 8 (h=7) → area = 7 × 7 = **49**

## Key Insight

Start with the **widest** container (pointers at both ends). The only way to potentially
find a larger container is to move the **shorter** line inward — moving the taller one
can never help because the water level is limited by the shorter side.

## Approach: Two Pointers (Greedy)

### Data Structures Used
- **Two index variables**: `left` and `right` — no extra data structures.

### Step-by-Step Logic

1. **Initialise** `left = 0`, `right = len(heights) - 1`, `max_water = 0`.
2. **While** `left < right`:
   - Calculate `width = right - left`.
   - Calculate `current_height = min(heights[left], heights[right])` (water limited by shorter line).
   - Calculate `current_water = current_height × width`.
   - Update `max_water` if `current_water` is larger.
   - **Move the shorter pointer inward**:
     - If `heights[left] < heights[right]`, increment `left`.
     - Otherwise, decrement `right`.
3. **Return** `max_water`.

### Why Move the Shorter Side?

Water volume = `min(left_height, right_height) × width`. When we move inward, width
decreases by 1. The only chance to increase volume is if `min(height)` increases enough
to compensate. Moving the taller line can't increase `min(height)`, so we move the shorter one.

### Walkthrough

```
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left=0(h=1) right=8(h=7): area = min(1,7)×8 = 8   max=8   → move left (shorter)
left=1(h=8) right=8(h=7): area = min(8,7)×7 = 49  max=49  → move right (shorter)
left=1(h=8) right=7(h=3): area = min(8,3)×6 = 18  max=49  → move right
left=1(h=8) right=6(h=8): area = min(8,8)×5 = 40  max=49  → move right
left=1(h=8) right=5(h=4): area = min(8,4)×4 = 16  max=49  → move right
left=1(h=8) right=4(h=5): area = min(8,5)×3 = 15  max=49  → move right
left=1(h=8) right=3(h=2): area = min(8,2)×2 = 4   max=49  → move right
left=1(h=8) right=2(h=6): area = min(8,6)×1 = 6   max=49  → move right
left=1 right=1 → pointers crossed, stop

Output: 49
```

## Edge Cases
- **Two elements** `[1, 1]` → area = `min(1,1) × 1 = 1`.
- **Decreasing heights** `[5, 4, 3, 2, 1]` → widest container is best.

## Complexity
- **Time**: O(n) — each pointer moves at most n times total.
- **Space**: O(1) — only a few variables.
