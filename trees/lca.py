
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Finds the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST).
        Assumes both p and q are present in the tree.

        Because it's a BST:
        - If both values are greater than current, move right.
        - If both values are less than current, move left.
        - If split occurs, current node is the LCA.

        Time Complexity: O(h), where h is the height of the tree.
        Space Complexity: O(1)

        Args:
            root (TreeNode): Root node of the BST.
            p (TreeNode): First target node.
            q (TreeNode): Second target node.

        Returns:
            TreeNode: The lowest common ancestor node.
        """
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
