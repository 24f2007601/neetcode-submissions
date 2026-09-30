from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Concatenate the array with itself using Python's list + operator
        # Produces a new list of length 2n: [nums[0]..nums[n-1], nums[0]..nums[n-1]]
        return nums + nums 

        