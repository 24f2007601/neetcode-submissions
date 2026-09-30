# String Encode and Decode — Solution Explanation

## Problem

Design an algorithm to **encode** a list of strings into a single string,
and **decode** that single string back into the original list.
The encoding must handle any characters (including delimiters) inside the strings.

**Example**: `["hello", "world"]` → encode → `"5#hello5#world"` → decode → `["hello", "world"]`

## Key Insight

Use a **length-prefixed protocol**: before each string, write its length followed by a
`#` delimiter. During decoding, read the length first, then extract exactly that many
characters. This avoids ambiguity even if the strings contain `#` or digits.

## Approach: Length-Prefix Encoding

### Encode — Step-by-Step

1. **Initialise** an empty string `encoded_string`.
2. **For each** string `s` in the input list:
   - Append `f"{len(s)}#{s}"` — the length, a `#` separator, then the string itself.
3. **Return** the concatenated `encoded_string`.

### Decode — Step-by-Step

1. **Initialise** an empty list `decoded_strs` and index `i = 0`.
2. **While** `i < len(s)`:
   - Find the position `j` of the next `#` character starting from `i`.
   - Parse the length: `length = int(s[i:j])`.
   - The actual string starts at `j + 1` and has exactly `length` characters.
   - Append `s[j+1 : j+1+length]` to `decoded_strs`.
   - Move `i` past the extracted string: `i = j + 1 + length`.
3. **Return** `decoded_strs`.

### Walkthrough

```
Encode: ["hello", "world"]
  "hello" → len=5 → "5#hello"
  "world" → len=5 → "5#world"
  encoded = "5#hello5#world"

Decode: "5#hello5#world"
  i=0: find '#' at j=1, length=5, extract s[2:7]="hello", i=7
  i=7: find '#' at j=8, length=5, extract s[9:14]="world", i=14
  decoded = ["hello", "world"] ✓
```

### Handling Edge Cases in Encoding

```
Encode: ["a#b", "12"]
  "a#b" → len=3 → "3#a#b"
  "12"  → len=2 → "2#12"
  encoded = "3#a#b2#12"

Decode: "3#a#b2#12"
  i=0: find '#' at j=1, length=3, extract s[2:5]="a#b", i=5    ← '#' inside string handled correctly
  i=5: find '#' at j=6, length=2, extract s[7:9]="12", i=9
  decoded = ["a#b", "12"] ✓
```

## Edge Cases
- **Empty strings in list** `["", "a"]` → `"0#1#a"` → decodes correctly.
- **Strings containing `#` or digits** → length-prefix makes decoding unambiguous.
- **Empty list** `[]` → encoded = `""` → decode returns `[]`.

## Complexity
- **Time**: O(n) for both encode and decode, where n = total characters across all strings.
- **Space**: O(n) for the encoded string / decoded list.
