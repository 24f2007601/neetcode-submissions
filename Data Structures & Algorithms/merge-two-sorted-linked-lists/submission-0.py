from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node provides a fixed start point to simplify edge cases
        dummy = ListNode()
        tail = dummy 

        # Traverse both lists, attaching the smaller node to tail
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next 

        # Attach any remaining elements from either list
        tail.next = list1 if list1 else list2

        return dummy.next