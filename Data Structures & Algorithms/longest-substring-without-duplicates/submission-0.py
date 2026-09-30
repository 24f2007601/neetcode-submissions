class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to track characters currently in the sliding window
        char_set = set()
        # Left boundary of the sliding window
        left = 0 
        max_length = 0 

        for right in range(len(s)):
            # If s[right] is already in the window, shrink from the left
            # until the duplicate is removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1 

            # Add the new character to the window
            char_set.add(s[right])

            # Update the longest valid window length found so far
            max_length = max(max_length, right - left + 1)

        return max_length        