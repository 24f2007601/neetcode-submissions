from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search: the minimum is at the rotation pivot point
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # Mid is in the left (higher) sorted half — minimum is to the right
                left = mid + 1
            else:
                # Mid is in the right (lower) sorted half — minimum is at mid or left of it
                right = mid

        # left == right — converged on the minimum element
        return nums[left]