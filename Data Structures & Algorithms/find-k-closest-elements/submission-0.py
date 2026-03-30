class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        delta = [(0,0)] * len(arr)
        res = []

        for i, num in enumerate(arr):
            delta[i] = (abs(x - num), num)
        
        delta.sort(key = lambda x:x[0])
        print(delta)

        for i in range(k):
            dist, pos = delta[i]
            res.append(pos)

        res.sort()
        return res

