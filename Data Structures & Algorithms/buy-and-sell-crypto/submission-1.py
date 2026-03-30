class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        if not isinstance(prices, list) or len(prices) < 2:
            return 0

        maxProfit = 0
        minValue = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - minValue
            maxProfit = max(profit, maxProfit)

            minValue = min(prices[i], minValue)
            


        return maxProfit