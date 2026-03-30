from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len1 = len(s1)
        hash1 = defaultdict(int)

        lenWindow = 0
        window = defaultdict(int)


        for c in s1:
            hash1[c] += 1


        for i in range(len(s2)):
            window[s2[i]] += 1
            lenWindow += 1
            if lenWindow > len1:
                char = s2[i - len1]
                window[char] -= 1
                if window[char] == 0:
                    del window[char]

            if window == hash1:
                return True

        return False







