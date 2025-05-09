from typing import List

class Solution:
    """
    Finds the length of the longest consecutive sequence in an unsorted list of integers.
    Uses a set for O(1) lookups and ensures O(n) time complexity by only starting chains
    at sequence starts.
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Returns the length of the longest consecutive elements sequence.
        Time: O(n), Space: O(n)
        """
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:  # start of a sequence
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(sol.longestConsecutive(nums))  # Expected: 4 (sequence: 1, 2, 3, 4)
