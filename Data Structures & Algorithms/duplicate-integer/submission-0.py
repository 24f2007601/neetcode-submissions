from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Track every number we've encountered so far
        seen = set()
        for num in nums:
            # If this number was already seen, a duplicate exists
            if num in seen:
                return True 
            # Record this number for future duplicate checks
            seen.add(num)
        # No duplicates found after scanning the entire array
        return False