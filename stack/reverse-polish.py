"""
LeetCode 150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note:
- The division between two integers always truncates toward zero.
- You may assume that the given RPN expression is always valid.
- The answer will not overflow (32-bit signed integer range).

Example:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: (2 + 1) * 3 = 9

redid this one 5/16/25. pretty easy but i found a better way updated below
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: b-a,
        '/': lambda a, b: int(b/a),
        '*': lambda a, b: a * b
        }

        for token in tokens:
            if token in ops:
                stack.append(ops[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        return stack[0]

        # for token in tokens:
        #     if token == '+':
        #         stack.append(stack.pop() + stack.pop())
        #     elif token == '-':
        #         right, left = stack.pop(), stack.pop()
        #         stack.append(left - right)
        #     elif token == '*':
        #         stack.append(stack.pop() * stack.pop())
        #     elif token == '/':
        #         right, left = stack.pop(), stack.pop()
        #         stack.append(int(left / right))  # Truncate toward zero
        #     else:
        #         stack.append(int(token))

        return stack[0]


if __name__ == "__main__":
    s = Solution()
    test = ["2", "1", "+", "3", "*"]  # (2 + 1) * 3 = 9
    print("Result:", s.evalRPN(test))  # → 9
