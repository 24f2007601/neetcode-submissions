from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Pointers to track the reversed portion and current node
        prev = None 
        curr = head 

        while curr:
            # Store next node before breaking the link
            nxt = curr.next
            # Reverse the pointer to point backwards
            curr.next = prev 
            # Move pointers forward
            prev = curr 
            curr = nxt 

        # prev points to the new head of the reversed list
        return prev