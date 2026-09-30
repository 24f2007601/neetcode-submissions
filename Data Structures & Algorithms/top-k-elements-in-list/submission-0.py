from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Step 2: Bucket sort — index i holds numbers that appear exactly i times
        # Max possible frequency is len(nums), so we need len(nums)+1 buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Step 3: Collect results from highest-frequency bucket downward
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                # Return as soon as we have k elements
                if len(result) == k:
                    return result