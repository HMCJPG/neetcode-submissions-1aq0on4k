class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices or len(prices) < 2:
            return 0

        minPrice = float('inf') # Sentinel
        maxProfit = 0

        for i, price in enumerate(prices):
            profit = price - minPrice
            maxProfit= max(maxProfit, profit)
            if price < minPrice:
                minPrice = price

        return maxProfit
            