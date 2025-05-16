from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        LeetCode 74. Search a 2D Matrix
        https://leetcode.com/problems/search-a-2d-matrix/

        Each row of the matrix is sorted, and the first integer of each row is greater 
        than the last integer of the previous row. This means the matrix can be treated
        as a flat sorted list for binary search.

        Time Complexity: O(log(m*n))
        Space Complexity: O(1)
        """

        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
