from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Compute the maximum depth of a binary tree.

        Args:
            root (Optional[TreeNode]): Root node of the binary tree.

        Returns:
            int: Maximum depth from root to a leaf node.

        Reviewed: 2025-05-17
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
