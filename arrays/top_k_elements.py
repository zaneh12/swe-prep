from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
        """

        buckets = [[] for bucket in range(len(nums)+1)] # O(N)

        freqmap = Counter(nums) #O(N)

        for number, freq in freqmap.items(): # O(N)
            buckets[freq].append(number)

        res = []

        for i in range(len(nums),0,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res

if __name__ == "__main__":
    sol = Solution()
    # Standard case
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], k=2))      # expected: [1, 2]

    # All elements have same frequency — ties allowed
    print(sol.topKFrequent([4, 4, 5, 5, 6, 6], k=2))      # expected: any 2 of [4, 5, 6]

    # Only one element
    print(sol.topKFrequent([1], k=1))                    # expected: [1]

    # Elements with decreasing frequency
    print(sol.topKFrequent([5, 5, 4, 4, 4, 3, 3, 2, 1], k=3))  # expected: [4, 5, 3]

    # All distinct elements, k = 3
    print(sol.topKFrequent([10, 20, 30, 40, 50], k=3))    # expected: any 3 of [10, 20, 30, 40, 50]

    # Frequency tie, check stability
    print(sol.topKFrequent([1, 2, 3, 1, 2, 3], k=2))      # expected: any 2 of [1, 2, 3]




