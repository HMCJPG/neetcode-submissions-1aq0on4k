from collections import defaultdict
from typing import Mapping

class Solution:

    def checkInvariant(self, SMap: Mapping[str, int], TMap: Mapping[str, int]) -> bool:
        for c in TMap:
            if SMap[c] < TMap[c]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:

        sMap = defaultdict(int)
        tMap = defaultdict(int)
        window = 0
        minSize = float("inf")
        prunedIndex = 0
        minString = ""

        # First, we will convert the string t into a hashmap.
        for c in t:
            tMap[c] += 1
        
        for i, c in enumerate(s):
            # Add the current character into the window
            sMap[c] += 1
            window += 1


            # Implement a way of checking the invariant here
            invariant = self.checkInvariant(sMap, tMap)

            while invariant == True:

                windowSize = i - prunedIndex + 1

                if windowSize < minSize:
                    minSize = windowSize
                    bestStart = prunedIndex
                
                sMap[s[prunedIndex]] -= 1
                prunedIndex += 1

                # Similarly, we need to use the check for the invariant
                invariant = self.checkInvariant(sMap, tMap)


        return "" if minSize == float("inf") else s[bestStart:bestStart + minSize]



















            
