# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determines whether subRoot is a subtree of root.

        A subtree of a binary tree is a tree that consists of a node in root and
        all of this node's descendants. The tree root could also be considered a subtree of itself.

        Args:
            root (Optional[TreeNode]): The root of the main binary tree.
            subRoot (Optional[TreeNode]): The root of the subtree to check.

        Returns:
            bool: True if subRoot is a subtree of root, False otherwise.
        """
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not root:
            return False

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
