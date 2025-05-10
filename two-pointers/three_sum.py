# /two_pointers/three_sum.py

from typing import List

class Solution:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    """
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif curSum < 0:
                    l += 1
                else:
                    r -= 1

        return res

if __name__ == "__main__":
    sol = Solution()
    example = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(example))  # Output: [[-1, -1, 2], [-1, 0, 1]]
