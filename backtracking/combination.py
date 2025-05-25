from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates where the chosen numbers sum to the target.
        Each number may be used an unlimited number of times.

        Uses backtracking with depth-first search:
        - At each step, we decide to include the current candidate or skip it.
        - We allow repeated use of the same candidate by not incrementing the index in the first dfs call.
        - We backtrack by popping the last candidate and trying the next one.

        Time Complexity: O(2^T), where T is the target (exponential in the worst case)
        Space Complexity: O(T) for the recursion stack

        Args:
            candidates (List[int]): List of positive integers (no duplicates).
            target (int): The desired sum.

        Returns:
            List[List[int]]: All unique combinations that sum to the target.
        """
        res = []

        def dfs(i: int, cur: List[int], total: int):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            # Include current candidate
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])  # reuse allowed

            # Backtrack and try next candidate
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
