# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Returns True if there are any duplicate elements in the list.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([7,1,5,3,6,4]))  # expected:False
    print(sol.containsDuplicate([1,2,3,1]))  # expected:True
    print(sol.containsDuplicate([1,2,3,4]))  # expected:False
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # expected:True

    