from typing import List

class Solution:
    """
    Returns a new list such that each element at index i is the product of all
    elements in the input list except nums[i], without using division.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Computes the product of all elements except self for each position.
        Time: O(n), Space: O(1) extra (output list not counted as extra space).
        """
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, 3]
    result = sol.productExceptSelf(nums)
    print(result)  # Expected output: [0, -6, 0, 0, 0]
