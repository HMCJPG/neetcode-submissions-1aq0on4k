class Solution:
    def numDecodings(self, s: str) -> int:
        

        n = len(s)

        if not s or s[0] == "0":
            return 0

        
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1


        for i in range(2, n + 1):

            one_digit = s[i - 1]
            two_digit = s[i - 2:i]

            if one_digit != '0':
                dp[i] += dp[i - 1]

            if two_digit[0] != "0" and 1 <= int(two_digit) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]



