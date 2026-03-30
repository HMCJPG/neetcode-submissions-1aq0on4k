from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        window = defaultdict(int)
        length = 0
        maxLength = 0

        lp, rp = 0, 0

        for i, c in enumerate(s):
            window[c] += 1
            length += 1
            rp += 1


            while max(window.values()) > 1:
                window[s[lp]] -= 1
                length -= 1
                lp += 1

            maxLength = max(maxLength, length)

        return maxLength
            