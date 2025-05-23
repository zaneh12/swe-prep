# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the n-th node from the end of a singly linked list.
        Uses a two-pointer technique with a dummy node to handle all edge cases cleanly,
        including when the head itself needs to be removed.

        Time Complexity: O(L), where L is the length of the list
        Space Complexity: O(1)

        Args:
            head (Optional[ListNode]): Head of the singly-linked list.
            n (int): Index from the end of the node to be removed.

        Returns:
            Optional[ListNode]: The head of the modified list.
        """
        dummy = ListNode(0, head)
        first = second = dummy

        # Create a gap of n between first and second
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first hits the end
        while first:
            first = first.next
            second = second.next

        # Remove the node after second
        second.next = second.next.next

        return dummy.next
