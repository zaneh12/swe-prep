from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform level order traversal (BFS) on a binary tree.
        Returns a list of lists, where each inner list contains the values of nodes at that depth.
        """
        res = []

        # Use a queue to process nodes level by level
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()

                if node:
                    # Append the current node's value to this level's list
                    level.append(node.val)

                    # Queue the child nodes (even if they're None)
                    q.append(node.left)
                    q.append(node.right)

            # Only append non-empty levels (skip levels of all-None placeholders)
            if level:
                res.append(level)

        return res
if __name__ == "__main__":
    # Example Tree:
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    sol = Solution()
    print(sol.levelOrder(root))  # Output: [[1], [2, 3], [4, 5]]
