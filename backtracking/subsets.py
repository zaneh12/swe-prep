from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible subsets (the power set) of the input list using backtracking.

        Backtracking tree structure for input [1]:
        
                  []
                 /  \
              [1]   []

        At each step:
        - Include nums[i] in the current subset and recurse.
        - Backtrack (remove nums[i]) and recurse without including it.

        Time Complexity: O(2^n)
        Space Complexity: O(n) for the recursion stack (excluding output)

        Args:
            nums (List[int]): List of unique integers.

        Returns:
            List[List[int]]: All possible subsets of the input list.
        """
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
