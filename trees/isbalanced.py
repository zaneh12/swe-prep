from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Returns True if the binary tree is height-balanced.

        A binary tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
        """
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)
        
        return dfs(root) != -1
