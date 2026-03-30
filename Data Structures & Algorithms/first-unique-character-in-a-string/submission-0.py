from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        map = defaultdict(list)

        for i,c in enumerate(s):

            map[c].append(i)

        for key, values in map.items():
            if len(values) == 1:
                return values[0]
            


        return -1