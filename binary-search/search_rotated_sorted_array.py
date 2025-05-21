# search_rotated_sorted_array.py

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Performs binary search in a rotated sorted array with no duplicates.
        Returns the index of target if found, else -1.

        Reviewed 5/21/2025
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 5, 1]
    target = 3
    print("Target found at index:", sol.search(nums, target))  # Output: 0
