import heapq
import math
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []
        res = []
        distance_map = defaultdict(list)

        for pair in points:
            x = pair[0]
            y = pair[1]
            paired = (x,y)

            distance = math.sqrt(
                ((x - 0)**2) +
                ((y - 0)**2)
            )

            distances.append((distance, pair))
            

        heapq.heapify(distances)


        for i in range(k):
            res.append(heapq.heappop(distances)[1])

        return res



