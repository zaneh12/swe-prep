from typing import List

class Solution:
    """
    Given a sorted array 'numbers' and a target, return the 1-based indices of two numbers 
    such that they add up to target. Assumes exactly one solution exists.
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            need = target - numbers[left]
            if need == numbers[right]:
                return [left + 1, right + 1]
            elif need < numbers[right]:
                right -= 1
            else:
                left += 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
