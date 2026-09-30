from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Length-prefix protocol: each string is stored as "{length}#{string}"
        # This handles any characters (including '#' and digits) inside strings
        encoded_string = ""
        for s in strs:
            # Prepend the string's length and a '#' delimiter before the string
            encoded_string += f"{len(s)}#{s}"
        return encoded_string 

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0 

        while i < len(s):
            # Find the '#' delimiter — everything before it is the length
            j = s.find('#', i)
            # Parse the length of the next string
            length = int(s[i:j])
            # Extract exactly 'length' characters after the '#'
            start_of_str = j + 1 
            end_of_str = start_of_str + length 
            decoded_strs.append(s[start_of_str:end_of_str])
            # Advance past the extracted string for the next iteration
            i = end_of_str

        return decoded_strs