from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # Initialise output with 1s — will accumulate prefix and suffix products
        output = [1] * length 

        # --- Prefix pass (left → right) ---
        # After this pass, output[i] = product of all elements BEFORE index i
        prefix = 1 
        for i in range(length):
            output[i] = prefix 
            prefix *= nums[i]

        # --- Suffix pass (right → left) ---
        # Multiply each output[i] by the product of all elements AFTER index i
        suffix = 1 
        for i in range(length - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        # Each output[i] now equals product(nums) / nums[i], computed without division
        return output 