class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        ans = 0

        def expand(l: int, r: int) -> int:

            count = 0

            while l >= 0 and r < n and s[l] == s[r]:

                count += 1
                l -= 1
                r += 1

            return count

        for i in range(n):
            ans += expand(i,i)
            ans += expand(i, i + 1)

        return ans