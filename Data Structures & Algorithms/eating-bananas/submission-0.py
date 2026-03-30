class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
    
        def pileEaten(k: int) -> bool:
            return sum(math.ceil(pile / k) for pile in piles) <= h

        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2

            if pileEaten(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo