from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the values of the nodes visible from the right side of the binary tree.
        This uses level-order traversal (BFS) and appends the last node value of each level.
        """
        res = []
        if not root:
            return res

        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # If it's the last node in this level, it's visible from the right
                if i == level_size - 1:
                    res.append(node.val)

                # Add child nodes for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res

# Example usage
if __name__ == "__main__":
    # Example Tree:
    #     1
    #    / \
    #   2   3
    #    \   \
    #     5   4

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    sol = Solution()
    result = sol.rightSideView(root)
    print("Right side view:", result)  # Output: [1, 3, 4]
