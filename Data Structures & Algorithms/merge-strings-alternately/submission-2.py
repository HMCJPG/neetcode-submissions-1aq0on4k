class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n1, n2 = len(word1), len(word2)
        res = ""

        if n1 == n2:
            for i in range(n1):
                res += word1[i]
                res += word2[i]
            return res


        elif n1 > n2:
            delta = n1 - n2
            leftover = word1[n1 - delta:n1]
            for i in range(n2):
                res += word1[i]
                res += word2[i]
            res += leftover
            return res

        elif n1 < n2:
            delta = n2 - n1
            leftover = word2[n2 - delta:n2]
            for i in range(n1):
                res += word1[i]
                res += word2[i]
            res += leftover
            return res


