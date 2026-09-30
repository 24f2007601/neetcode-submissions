class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency map for characters in the current sliding window
        count = {}
        max_len = 0
        # Tracks the highest frequency of any single character in the window
        max_freq = 0
        left = 0

        for right in range(len(s)):
            # Expand window: include s[right] and update its frequency
            count[s[right]] = 1 + count.get(s[right], 0)
            # Update the max frequency of any character in the current window
            max_freq = max(max_freq, count[s[right]])

            # If characters to replace (window_size - max_freq) exceeds k,
            # the window is invalid — shrink from the left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update the best valid window length found so far
            max_len = max(max_len, right - left + 1)

        return max_len