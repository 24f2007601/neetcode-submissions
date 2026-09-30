# Validate Parentheses — Solution Explanation

## Problem

Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[`, `]`,
determine if the input string is **valid**. A string is valid if:
- Every open bracket is closed by the same type of bracket.
- Open brackets are closed in the correct (LIFO) order.
- Every close bracket has a corresponding open bracket.

**Example**: `"()[]{}"` → `True` | `"(]"` → `False` | `"([)]"` → `False`

## Key Insight

A **stack** naturally handles nested/matching brackets (LIFO order). Push open brackets
onto the stack. When a closing bracket appears, pop the stack and check if it matches.
If the stack is empty at the end, all brackets were properly matched.

## Approach: Stack with Mapping

### Data Structures Used
- **`stack` (list)**: Holds unmatched opening brackets in LIFO order.
- **`mapping` dict**: Maps each closing bracket to its matching opening bracket.

### Step-by-Step Logic

1. **Create** an empty `stack` and a `mapping` dict: `)` → `(`, `}` → `{`, `]` → `[`.
2. **Iterate** through each character `char` in the string:
   - **If `char` is a closing bracket** (found in `mapping`):
     - Pop the top of the stack (or use `'#'` as a sentinel if stack is empty).
     - If the popped element doesn't match the expected opening bracket → return `False`.
   - **If `char` is an opening bracket**:
     - Push it onto the stack.
3. **Return** `not stack` — `True` if the stack is empty (all brackets matched), `False` otherwise.

### Why Use `'#'` as Sentinel?

If the stack is empty when we encounter a closing bracket, it means there's no matching
opening bracket. Using `'#'` avoids an `IndexError` on `pop()` and guarantees the
comparison `mapping[char] != '#'` will fail, correctly returning `False`.

### Walkthrough

```
Input: "({[]})"

char='(': opening → push → stack=['(']
char='{': opening → push → stack=['(', '{']
char='[': opening → push → stack=['(', '{', '[']
char=']': closing → pop '[', mapping[']']=']' matches '[' ✓ → stack=['(', '{']
char='}': closing → pop '{', mapping['}']='{' matches '{' ✓ → stack=['(']
char=')': closing → pop '(', mapping[')']=')' matches '(' ✓ → stack=[]

stack is empty → return True ✓
```

### Failure Example

```
Input: "([)]"

char='(': push → stack=['(']
char='[': push → stack=['(', '[']
char=')': closing → pop '[', mapping[')']='(' but got '[' → MISMATCH → return False ✗
```

## Edge Cases
- **Empty string** `""` → stack stays empty → `True`.
- **Only opening brackets** `"((("` → stack has 3 elements → `False`.
- **Only closing brackets** `")))"` → stack is empty on first pop, sentinel mismatch → `False`.
- **Single bracket** `"("` → `False`.

## Complexity
- **Time**: O(n) — single pass through the string.
- **Space**: O(n) — worst case all opening brackets pushed onto stack.
