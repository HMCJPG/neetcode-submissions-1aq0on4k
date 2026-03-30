from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.pointsList = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pointsList[tuple(point)] += 1

        

    def count(self, point: List[int]) -> int:

        (x,y) = point
        res = 0

        for (xi, yi), freq in list(self.pointsList.items()):
            if abs(x - xi) != abs(y - yi) or x == xi or y == yi:
                continue


            res += (freq * self.pointsList[(xi,y)] * self.pointsList[(x,yi)])

        return res















        
