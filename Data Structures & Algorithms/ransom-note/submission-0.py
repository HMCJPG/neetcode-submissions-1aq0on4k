from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

        ransomMap = defaultdict(int)
        magazineMap = defaultdict(int)

        for c in ransomNote:
            ransomMap[c] += 1

        for c in magazine:
            magazineMap[c] += 1

        return all(ransomMap[c] <= magazineMap[c] for c in ransomMap)