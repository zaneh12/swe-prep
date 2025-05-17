from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Compute the diameter (longest path between any two nodes) of a binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The diameter in number of edges.
        """
        self.max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # Update the max diameter at this node
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            # Return the depth for use by parent node
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.max_diameter

# Example usage and test case
if __name__ == '__main__':
    # Construct tree:
    #       1
    #        \
    #         2
    #        / \
    #       3   4
    #      /
    #     5

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(5)

    sol = Solution()
    print("Diameter of binary tree:", sol.diameterOfBinaryTree(root))  # Expected output: 3
