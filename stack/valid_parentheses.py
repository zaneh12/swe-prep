# /stack/valid_parentheses.py

from typing import List

class Solution:
    """
    Check if a string of brackets is valid.
    A string is valid if every opening bracket has a matching closing bracket in the correct order.
    """

    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for c in s:
            if c in closeToOpen:
                # If there's no matching open bracket, or it's the wrong one → invalid
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket → push to stack
                stack.append(c)

        # If stack is empty, all brackets were matched
        return not stack

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("({})"))   # True
    print(sol.isValid("({}"))    # False
    print(sol.isValid("({[()]})"))  # True
    print(sol.isValid("((("))    # False
