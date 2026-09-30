from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0 
        # Two pointers starting at the widest possible container
        left = 0 
        right = len(heights) - 1

        while left < right:
            # Width is the horizontal distance between the two lines
            width = right - left 
            # Water level is limited by the shorter of the two lines
            current_height = min(heights[left], heights[right])
            # Area of the container formed by these two lines
            current_water = current_height * width 
            # Track the maximum water area seen so far
            max_water = max(max_water, current_water)

            # Move the shorter line inward — moving the taller one
            # can never increase the min(height), so it can't help
            if heights[left] < heights[right]:
                left += 1 
            else:
                right -= 1

        return max_water