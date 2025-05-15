from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # Value stored in the node
        self.next = next    # Pointer to the next node


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list in-place.

        Args:
            head (ListNode): Head of the input linked list.

        Returns:
            ListNode: New head of the reversed linked list.
        """
        prev = None          # Will become the new head
        curr = head          # Start from the original head

        while curr:
            next_node = curr.next  # Temporarily store the next node
            curr.next = prev       # Reverse the pointer
            prev = curr            # Move prev up
            curr = next_node       # Move curr up

        return prev  # New head of the reversed list
