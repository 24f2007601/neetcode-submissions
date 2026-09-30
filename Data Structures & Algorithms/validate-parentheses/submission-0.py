class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to track unmatched opening brackets in LIFO order
        stack = []
        # Maps each closing bracket to its matching opening bracket
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Closing bracket found — pop the top of the stack
                # Use '#' sentinel if stack is empty (no matching opener → will fail check)
                top_element = stack.pop() if stack else '#'
                # If the popped element doesn't match the expected opening bracket → invalid
                if mapping[char] != top_element:
                    return False
            else:
                # Opening bracket — push onto stack to be matched later
                stack.append(char)
                
        # Valid only if all opening brackets were matched (stack is empty)
        return not stack
