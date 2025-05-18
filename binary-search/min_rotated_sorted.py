# find_min_rotated_sorted_array.py

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array with no duplicates.
        Binary search with a shrinking [l, r] window.
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            # If mid element is greater than the rightmost, min is to the right
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # min is at mid or to the left
                r = mid

        # Loop exits when l == r, which is the index of the smallest element
        return nums[l]

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 4, 5, 6, 1, 2]
    print("Minimum value:", sol.findMin(nums))  # Output should be 1
