class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        s = [c.lower() for c in s if c.isalnum()]

        lp = 0
        rp = len(s)-1 

        while lp < rp:
            if s[lp] != s[rp]:
                return False
            lp += 1
            rp -= 1

        return True
