from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # Node value
        self.next = next    # Pointer to the next node

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted linked list.

        Args:
            list1 (ListNode): Head of the first sorted linked list.
            list2 (ListNode): Head of the second sorted linked list.

        Returns:
            ListNode: Head of the merged sorted linked list.
        """
        dummy = ListNode()   # Dummy head to simplify logic
        tail = dummy         # Tail tracks the end of the merged list

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining non-empty list (if any)
        tail.next = list1 or list2

        return dummy.next    # Skip dummy and return the actual head
