class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def eatSuccess(k: int) -> bool:
            totalH = 0
            for pile in piles:
                totalH += math.ceil(pile / k)
            if totalH <= h:
                return True
            else:
                return False


        left = 1
        right = max(piles)

        while left <= right:
            middle = (left + right) // 2
            if eatSuccess(middle):
                right = middle - 1
            else:
                left = middle + 1 

        return left