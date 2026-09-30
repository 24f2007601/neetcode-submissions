# Valid Sudoku — Solution Explanation

## Problem

Determine if a 9×9 Sudoku board is valid. A board is valid if:
- Each **row** contains the digits 1-9 without repetition.
- Each **column** contains the digits 1-9 without repetition.
- Each of the nine 3×3 **sub-boxes** contains the digits 1-9 without repetition.

Only filled cells need to be validated (empty cells are `"."`).

## Key Insight

Use **three arrays of sets** — one for rows, one for columns, one for 3×3 boxes.
For each filled cell, check if the digit already exists in the corresponding row set,
column set, or box set. If it does, the board is invalid.

The trick is the **box index formula**: `box_idx = (row // 3) * 3 + (col // 3)`,
which maps each cell to one of the nine 3×3 boxes (indexed 0-8).

## Approach: Three Sets (Row, Column, Box)

### Data Structures Used
- **`rows[9]`**: Nine sets, one per row — `rows[r]` contains digits seen in row `r`.
- **`cols[9]`**: Nine sets, one per column — `cols[c]` contains digits seen in column `c`.
- **`boxes[9]`**: Nine sets, one per 3×3 box — `boxes[idx]` contains digits seen in that box.

### Step-by-Step Logic

1. **Create** three lists of 9 empty sets: `rows`, `cols`, `boxes`.
2. **Iterate** over every cell `(r, c)` in the 9×9 grid:
   - If the cell is `"."`, skip it.
   - Compute `box_idx = (r // 3) * 3 + (c // 3)`.
   - **Check**: if the digit is in `rows[r]` OR `cols[c]` OR `boxes[box_idx]` → return `False`.
   - **Add** the digit to all three sets.
3. If no duplicates found → return `True`.

### Box Index Formula Explained

```
Row 0-2, Col 0-2 → (0//3)*3 + (0//3) = 0  → Box 0
Row 0-2, Col 3-5 → (0//3)*3 + (3//3) = 1  → Box 1
Row 0-2, Col 6-8 → (0//3)*3 + (6//3) = 2  → Box 2
Row 3-5, Col 0-2 → (3//3)*3 + (0//3) = 3  → Box 3
Row 3-5, Col 3-5 → (3//3)*3 + (3//3) = 4  → Box 4
...
Row 6-8, Col 6-8 → (6//3)*3 + (6//3) = 8  → Box 8

Box layout:
┌───┬───┬───┐
│ 0 │ 1 │ 2 │
├───┼───┼───┤
│ 3 │ 4 │ 5 │
├───┼───┼───┤
│ 6 │ 7 │ 8 │
└───┴───┴───┘
```

### Walkthrough (partial)

```
Board cell (0,0) = "5":
  box_idx = (0//3)*3 + (0//3) = 0
  "5" not in rows[0], cols[0], boxes[0] → add to all three

Board cell (0,1) = "3":
  box_idx = 0
  "3" not in rows[0], cols[1], boxes[0] → add to all three

... if later cell (0,5) = "5":
  "5" already in rows[0] → return False (duplicate in row 0)
```

## Edge Cases
- **Completely empty board** → all cells are `"."` → `True`.
- **Valid but incomplete board** → only checks existing digits, not solvability.

## Complexity
- **Time**: O(1) — the board is always 9×9 = 81 cells (fixed size).
- **Space**: O(1) — sets hold at most 9 elements each (fixed size).
