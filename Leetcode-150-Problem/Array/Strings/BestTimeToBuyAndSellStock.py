class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Time- O(n), Space- O(1)
        # Leetcode-121: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
        # Copy the below code logic
        buyPos = 0
        sellPos = 1
        max_profit = 0
        while sellPos< len(prices):
            currProfit = prices[sellPos] - prices[buyPos]
            if prices[buyPos] < prices[sellPos]:
                max_profit = max(currProfit,max_profit)
            else:
                buyPos = sellPos
            sellPos += 1
        return max_profit