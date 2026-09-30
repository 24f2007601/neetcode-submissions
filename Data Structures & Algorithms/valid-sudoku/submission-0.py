from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Three arrays of sets to track digits seen in each row, column, and 3×3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Formula to map (row, col) to one of nine 3×3 box indices (0-8)
                # e.g. (0-2, 0-2) → box 0, (3-5, 3-5) → box 4, (6-8, 6-8) → box 8
                box_idx = (r // 3) * 3 + (c // 3)
                
                # If the digit already exists in the same row, column, or box → invalid
                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_idx]):
                    return False
                
                # Record the digit in all three tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        # No duplicates found in any row, column, or box → valid board
        return True 