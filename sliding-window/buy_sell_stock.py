from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit achievable from a single buy-sell transaction.

        :param prices: List of daily stock prices.
        :return: Maximum profit from one transaction.
        """
        l, r = 0, 1  # l = buy day, r = sell day
        best = 0

        while r < len(prices):
            if prices[r] >= prices[l]:
                profit = prices[r] - prices[l]
                best = max(profit, best)
            else:
                l = r
            r += 1

        return best

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
    print(sol.maxProfit([7, 6, 4, 3, 1]))     # Output: 0
