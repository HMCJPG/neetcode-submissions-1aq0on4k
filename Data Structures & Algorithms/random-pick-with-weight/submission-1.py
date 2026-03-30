import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.prefixSums = []
        self.current_weight = 0

        for weight in w:
            self.current_weight += weight
            self.prefixSums.append(self.current_weight)
        self.maxWeight = self.current_weight

            

    def pickIndex(self) -> int:
        target = random.randint(1, self.maxWeight)

        return bisect.bisect_left(self.prefixSums, target)


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()