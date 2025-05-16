from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Standard binary search implementation.
        Returns the index of target in nums if found, else -1.
        Assumes nums is sorted in ascending order.

        # redid this 05/16/25. need to remember 1. is len(nums) a valid index? 2. if mid!= target than l!= mid it mid+1
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2  # correct mid calculation to avoid overflow
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

# Test cases
if __name__ == "__main__":
    sol = Solution()

    print(sol.search([1, 3, 5, 7, 9], 7))     # Output: 3
    print(sol.search([1, 3, 5, 7, 9], 1))     # Output: 0
    print(sol.search([1, 3, 5, 7, 9], 9))     # Output: 4
    print(sol.search([1, 3, 5, 7, 9], 2))     # Output: -1
    print(sol.search([], 3))                 # Output: -1
