from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not isinstance(s, str) or len(s) == 0:
            return 0

        seen = {}
        lp = 0
        maxLen = 0
        globalMax = 0

        for i, c in enumerate(s):
            if c in seen and seen[c] >= lp:
                lp = seen[c] + 1
                maxLen = i - lp

 


            maxLen += 1
            
            
            seen[c] = i
            globalMax = max(globalMax, maxLen)
        

        return globalMax

