from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        LeetCode 875. Koko Eating Bananas
        https://leetcode.com/problems/koko-eating-bananas/

        Koko loves to eat bananas. There are 'piles', each with a certain number of bananas.
        She eats at a fixed speed 'k' bananas per hour, and she has 'h' hours to finish them all.
        The goal is to find the **minimum integer eating speed k** such that all bananas
        can be eaten within 'h' hours.

        This solution uses binary search over possible eating speeds from 1 to max(piles),
        and checks at each midpoint if the total time required is within 'h'.

        Parameters:
        - piles (List[int]): List of pile sizes
        - h (int): Number of hours available

        Returns:
        - int: Minimum eating speed k such that all bananas are eaten in h hours

        Time Complexity: O(n * log m), where:
            n = number of piles
            m = max(piles)
        Space Complexity: O(1)

        Reviewed on 2025-05-16.
        """

        l,r = 1, max(piles)
        res = r

        while l<=r:
            k = (r+l)//2
            hours = sum([math.ceil(p/k) for p in piles])

            if hours <= h: # this works, but maybe it can be smaller since we are in good time
                res = min(res, k) # to ensure but works without
                r = k-1
            else: # we took too much time and need to try a smaller option than the midpoint
                l = k+1

        return res






if __name__ == "__main__":
    s = Solution()

    # Test case 1: Basic example
    piles = [3, 6, 7, 11]
    h = 8
    print("Test 1:", s.minEatingSpeed(piles, h))  # Expected: 4

    # Test case 2: Just enough time
    piles = [30, 11, 23, 4, 20]
    h = 5
    print("Test 2:", s.minEatingSpeed(piles, h))  # Expected: 30

    # Test case 3: Plenty of time (should go down to 1)
    piles = [1, 1, 1, 1]
    h = 10
    print("Test 3:", s.minEatingSpeed(piles, h))  # Expected: 1

    # Test case 4: Large pile size (stress test)
    piles = [10**9]
    h = 2
    print("Test 4:", s.minEatingSpeed(piles, h))  # Expected: 500000000
