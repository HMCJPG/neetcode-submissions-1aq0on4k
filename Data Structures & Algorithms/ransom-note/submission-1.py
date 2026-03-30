from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

        rMap = Counter(ransomNote)
        mMap = Counter(magazine)

        return all(rMap[c] <= mMap[c] for c in rMap)