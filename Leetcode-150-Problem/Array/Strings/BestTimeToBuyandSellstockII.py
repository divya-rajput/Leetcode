class Solution:
    def maxProfit(self, prices: list[int]) -> int: 
        # Time- O(n), Space- O(1)
        # Leetcode-122: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
        # Copy the below code logic to Leetcode code editor
        i , j = 0, 1
        res = 0
        while j <= len(prices)-1 and i<j:
            val = prices[j] - prices[i]
            if val > 0:
                res += val
            i += 1
            j += 1
        return res