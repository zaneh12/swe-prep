from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given a list of integers and a target value, return the indices
        of the two numbers that add up to the target. Assumes exactly one solution exists.
        """
        num_to_index = {}  # Maps value to its index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], target=9))      # expected: [0, 1]
    print(sol.twoSum([3, 2, 4], target=6))           # expected: [1, 2]
    print(sol.twoSum([3, 3], target=6))              # expected: [0, 1]
