class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings and compare — anagrams produce identical sorted sequences
        # e.g. sorted("anagram") == sorted("nagaram") → both become ['a','a','a','g','m','n','r']
        return sorted(s) == sorted(t)