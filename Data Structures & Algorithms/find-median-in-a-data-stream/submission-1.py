import bisect

class MedianFinder:

    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.vals, num)
        

    def findMedian(self) -> float:
        if len(self.vals) % 2 == 0:
            midIndex1, midIndex2 = len(self.vals) // 2, (len(self.vals) // 2) - 1
            median = (self.vals[midIndex1] + self.vals[midIndex2]) / 2
            return median

        else:
            midIndex = len(self.vals) // 2
            return self.vals[midIndex]
        
        