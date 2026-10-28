# Reverse a Linked List — Solution Explanation

## Problem

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

**Example**: `head = [0, 1, 2, 3]` → `[3, 2, 1, 0]`

## Key Insight

As we traverse the list, each node needs its `next` pointer redirected to point to the previous node instead of the next one. We can do this in-place using two main pointers (`prev` and `curr`), along with a temporary pointer (`nxt`) to preserve the remaining unreversed list.

## Approach: Iterative In-Place Reversal

### Data Structures Used
- **`prev`**: Tracks the node immediately preceding `curr` (initially `None` as the original head becomes the tail).
- **`curr`**: The current node whose pointer is being reversed.
- **`nxt`**: Temporary reference to `curr.next` to avoid losing the rest of the list when modifying `curr.next`.

### Step-by-Step Logic

1. **Initialize** `prev = None` and `curr = head`.
2. **Iterate** while `curr` is not `None`:
   - Save the next node: `nxt = curr.next`.
   - Reverse the link: `curr.next = prev`.
   - Advance `prev`: `prev = curr`.
   - Advance `curr`: `curr = nxt`.
3. **Return** `prev`, which now points to the new head of the reversed list.

### Walkthrough

```
Initial: 0 -> 1 -> 2 -> None
prev = None, curr = 0

Iteration 1:
  nxt = 1
  curr.next = None (0 -> None)
  prev = 0
  curr = 1

Iteration 2:
  nxt = 2
  curr.next = 0 (1 -> 0 -> None)
  prev = 1
  curr = 2

Iteration 3:
  nxt = None
  curr.next = 1 (2 -> 1 -> 0 -> None)
  prev = 2
  curr = None

Loop ends (curr is None). Return prev (2).
Result: 2 -> 1 -> 0 -> None
```

## Edge Cases
- **Empty list**: `head = None` → loop does not execute; returns `prev` (`None`).
- **Single-node list**: `head = [1]` → loop executes once; `1.next` becomes `None`; returns `1`.
- **Two nodes**: `head = [1, 2]` → cleanly reverses to `2 -> 1`.

## Complexity
- **Time**: O(n) — single pass visiting each of the n nodes once.
- **Space**: O(1) — purely pointers manipulated in-place with no extra memory.
