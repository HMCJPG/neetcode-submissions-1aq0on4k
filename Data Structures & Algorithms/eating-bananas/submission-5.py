class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eaten(k: int) -> bool:

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours > h:
                return False
            else:
                return True

        left, right = 1, max(piles)

        while left <= right:

            mid = (left + right) // 2

            if eaten(mid):
                right = mid - 1
            
            else:
                left = mid + 1

        return left









