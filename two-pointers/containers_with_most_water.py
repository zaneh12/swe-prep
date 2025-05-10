# /two_pointers/container_with_most_water.py

from typing import List

class Solution:
    """
    Given a list of heights, return the maximum area of water that can be contained
    between two lines. The width is the distance between lines, and the height is
    the shorter of the two lines.
    """

    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            area = height * width
            max_area = max(max_area, area)

            # Move the shorter pointer inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area

if __name__ == "__main__":
    sol = Solution()
    example = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(example))  # Output: 49
