class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        s_index = 0

        for i in range(len(t)):
            if s_index < len(s) and t[i] == s[s_index]:
                s_index += 1

        return s_index == len(s)
