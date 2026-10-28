from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash map: sorted-character tuple → list of original strings
        anagram_map = defaultdict(list)

        for s in strs:
            # Sort characters to create a canonical key shared by all anagrams
            # Convert to tuple because lists are not hashable (can't be dict keys)
            sorted_key = tuple(sorted(s))
            # Group the original string under its canonical key
            anagram_map[sorted_key].append(s)

        # Return all grouped anagram lists
        return list(anagram_map.values())
