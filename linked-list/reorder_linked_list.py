# reorder_linked_list.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rearrange(head):
    """
    Reorders a singly linked list in-place to the pattern:
    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

    The function modifies the list by:
    1. Finding the middle node.
    2. Reversing the second half of the list.
    3. Merging the two halves alternately.

    Parameters:
    head (ListNode): The head of the singly linked list.

    Returns:
    None

    Reviewed on 5/20/2025 full grasp
    """
    if not head or not head.next:
        return

    # Step 1: Find the midpoint using slow/fast pointers
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    prev = None
    curr = slow.next
    slow.next = None  # Break the list into two parts

    while curr:
        position = curr.next
        curr.next = prev
        prev = curr
        curr = position

    # Step 3: Merge the two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
