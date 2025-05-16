from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        LeetCode 141. Linked List Cycle
        https://leetcode.com/problems/linked-list-cycle/

        Determines if a singly linked list contains a cycle using the 
        Floyd's Tortoise and Hare algorithm (fast and slow pointers).

        Parameters:
        - head (Optional[ListNode]): The head of the singly linked list.

        Returns:
        - bool: True if a cycle exists, False otherwise.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Reviewed and confirmed on 2025-05-16.
        """

        fast = head
        slow = head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
