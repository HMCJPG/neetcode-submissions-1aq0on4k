import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)


        while len(stones) > 1:

            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first != second:

                newStone = first - second

                if newStone > 0:
                    newStone = -newStone
                heapq.heappush(stones, newStone)

        return -stones[0] if stones else 0

