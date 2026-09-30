# Anagram Groups — Solution Explanation

## Problem

Given a list of strings, group all strings that are anagrams of each other together.
Two strings are anagrams if they contain the exact same characters in any order.

**Example**: `["eat","tea","tan","ate","nat","bat"]` → `[["eat","tea","ate"],["tan","nat"],["bat"]]`

## Key Insight

Two strings are anagrams if and only if their **sorted character sequences are identical**.
By sorting each string, we get a canonical "signature" that all anagrams share.

## Approach: Hash Map with Sorted Key

### Data Structures Used
- **`defaultdict(list)`**: Maps each sorted-character tuple to a list of original strings that share that signature.

### Step-by-Step Logic

1. **Initialise** a `defaultdict(list)` called `anagram_map`.
2. **Iterate** over every string `s` in the input list:
   - Sort the characters of `s` and convert to a **tuple** (tuples are hashable; lists are not).
   - This sorted tuple is the **canonical key** for all anagrams of `s`.
   - **Append** the original string `s` to `anagram_map[sorted_key]`.
3. **Return** all the grouped lists: `list(anagram_map.values())`.

### Walkthrough

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

"eat" → sorted = ('a','e','t') → map: {('a','e','t'): ["eat"]}
"tea" → sorted = ('a','e','t') → map: {('a','e','t'): ["eat","tea"]}
"tan" → sorted = ('a','n','t') → map: {('a','e','t'): ["eat","tea"], ('a','n','t'): ["tan"]}
"ate" → sorted = ('a','e','t') → map: {('a','e','t'): ["eat","tea","ate"], ...}
"nat" → sorted = ('a','n','t') → map: {..., ('a','n','t'): ["tan","nat"]}
"bat" → sorted = ('a','b','t') → map: {..., ('a','b','t'): ["bat"]}

Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

## Edge Cases
- **Empty input list** → return `[]`.
- **List with empty strings** `["", ""]` → both sort to `()`, grouped together.
- **All unique strings** → each group contains a single string.

## Complexity
- **Time**: O(N · K log K) — N strings, each of average length K (sorting each string).
- **Space**: O(N · K) — storing all strings in the hash map.
