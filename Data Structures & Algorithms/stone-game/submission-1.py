class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}

        def dp(left, right):

            if left > right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            advantage = max(
                piles[left] - dp(left + 1, right),
                piles[right] - dp(left, right - 1)
            )

            memo[(left, right)] = advantage
            return advantage

        return dp(0, len(piles) - 1) > 0
        