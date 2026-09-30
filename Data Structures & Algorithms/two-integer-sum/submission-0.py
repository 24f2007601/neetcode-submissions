from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map: number → index, for O(1) complement lookups
        num_map = {}

        for i, num in enumerate(nums):
            # The complement is the value we need to find to reach the target
            complement = target - num

            # If the complement was already seen, we found the two indices
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store current number and its index for future complement checks
            num_map[num] = i