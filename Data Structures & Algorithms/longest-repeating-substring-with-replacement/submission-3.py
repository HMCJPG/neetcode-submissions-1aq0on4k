from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        currentLength = 0
        maxLength = 0
        seen = defaultdict(int)
        lp = 0
        rp = 0
        for c in s:
            seen[c] += 1
            rp += 1

            windowSize = rp - lp
            currentLength += 1
            if windowSize - max(seen.values()) > k:
                seen[s[lp]] -= 1
                lp += 1
                currentLength -= 1

            if currentLength > maxLength:
                maxLength = currentLength

        return maxLength
            
            
            
            


        
        
    
