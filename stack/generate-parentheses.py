"""
LeetCode 22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Constraints:
- 1 <= n <= 8
"""

from typing import List

class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN: int, closedN: int):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParentheses(3))  # Example output: ["((()))","(()())","(())()","()(())","()()()"]
