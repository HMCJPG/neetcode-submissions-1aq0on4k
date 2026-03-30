import bisect


class MedianFinder:

    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.vals, num)
        

    def findMedian(self) -> float:
        
        if not self.vals:
            return 0

        n = len(self.vals)
        
        if n % 2 == 0:
            mI_1 = n // 2
            mI_2 = (n // 2) - 1

            median = (self.vals[mI_1] + self.vals[mI_2]) / 2
            return median

        else:
            mI = n // 2
            return self.vals[mI]

            














