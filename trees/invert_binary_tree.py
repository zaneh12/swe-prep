# invert_binary_tree.py

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert a binary tree by recursively swapping left and right subtrees.

        Args:
            root (Optional[TreeNode]): Root node of the binary tree.

        Returns:
            Optional[TreeNode]: Root of the inverted binary tree.
        """
        if not root:
            return None
        # Recursively invert left and right subtrees
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # Swap them
        root.left, root.right = right, left
        return root
