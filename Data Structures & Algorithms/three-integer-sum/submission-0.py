from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sorting enables the two-pointer technique and easy duplicate skipping
        nums.sort() 

        for i in range(len(nums)):
            # Early exit: if nums[i] > 0, no three positive numbers can sum to 0
            if nums[i] > 0:
                break
            # Skip duplicate values of nums[i] to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Two pointers on the subarray to the right of i
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum > 0:
                    # Sum too large — move right pointer left to decrease sum
                    r -= 1  
                elif three_sum < 0:
                    # Sum too small — move left pointer right to increase sum
                    l += 1 
                else:
                    # Found a valid triplet that sums to zero
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values of nums[l] to avoid duplicate triplets
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res