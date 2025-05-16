"""
LeetCode 739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures, return a list such that, for each day,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

Example:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

redid this one on 5/16/25. was good except i put the > sign backwards
need to focus on focus. think more critically. every char matters
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []  # stores (temperature, index)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                output[index] = i - index
            stack.append((t, i))

        return output


if __name__ == "__main__":
    sol = Solution()
    test_input = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(test_input))  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
