# Merge Two Sorted Linked Lists — Solution Explanation

## Problem

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

**Example**: `list1 = [1, 2, 4]`, `list2 = [1, 3, 4]` → `[1, 1, 2, 3, 4, 4]`

## Key Insight

Since both lists are already sorted, we can build the merged list incrementally using two pointers. By using a **dummy node**, we avoid edge-case handling for the head of the new list. At each step, we attach the smaller current node and advance its respective pointer.

## Approach: Iterative with Dummy Node

### Data Structures Used
- **`dummy` ListNode**: Acts as a fixed anchor preceding the merged list.
- **`tail` pointer**: Tracks the last appended node in the merged list.

### Step-by-Step Logic

1. **Initialize** a `dummy` node (`ListNode()`) and a `tail` pointer pointing to `dummy`.
2. **Iterate** while both `list1` and `list2` are not null:
   - Compare `list1.val` and `list2.val`.
   - If `list1.val < list2.val`:
     - Point `tail.next` to `list1`.
     - Advance `list1 = list1.next`.
   - Else:
     - Point `tail.next` to `list2`.
     - Advance `list2 = list2.next`.
   - Advance `tail = tail.next`.
3. **Attach Remainder**: Once one list is exhausted, attach the remainder of the non-empty list directly:
   - `tail.next = list1 if list1 else list2`.
4. **Return** `dummy.next` (the head of the newly merged list).

### Walkthrough

```
list1 = 1 -> 2 -> 4
list2 = 1 -> 3 -> 4
dummy -> None, tail = dummy

Step 1: list1.val (1) not < list2.val (1) -> attach list2(1)
        dummy -> 1 (from list2), tail = 1, list2 = 3
Step 2: list1.val (1) < list2.val (3) -> attach list1(1)
        dummy -> 1 -> 1, tail = 1, list1 = 2
Step 3: list1.val (2) < list2.val (3) -> attach list1(2)
        dummy -> 1 -> 1 -> 2, tail = 2, list1 = 4
Step 4: list1.val (4) not < list2.val (3) -> attach list2(3)
        dummy -> 1 -> 1 -> 2 -> 3, tail = 3, list2 = 4
Step 5: list1.val (4) not < list2.val (4) -> attach list2(4)
        dummy -> 1 -> 1 -> 2 -> 3 -> 4, tail = 4, list2 = None
End Loop: attach remaining list1 (4)
        dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4

Result: dummy.next -> [1, 1, 2, 3, 4, 4]
```

## Edge Cases
- **Both lists empty**: `list1 = None, list2 = None` → loop doesn't run, attaches `None`, returns `None`.
- **One list empty**: `list1 = None, list2 = [0]` → loop doesn't run, attaches `list2`, returns `[0]`.
- **Unequal lengths**: Remaining nodes of the longer list are appended in O(1) time.

## Complexity
- **Time**: O(n + m) — single pass where n and m are lengths of `list1` and `list2`.
- **Space**: O(1) — we splice existing nodes without allocating new nodes (except the single dummy anchor).
