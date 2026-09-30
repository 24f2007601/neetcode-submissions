class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers: one at start, one at end
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
           
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters in lowercase — if mismatch, not a palindrome
            if s[left].lower() != s[right].lower():
                return False
            
            # Both characters matched — move pointers inward
            left += 1
            right -= 1
            
        # All character pairs matched — the string is a valid palindrome
        return True
