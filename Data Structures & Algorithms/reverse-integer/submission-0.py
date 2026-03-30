class Solution:
    def reverse(self, x: int) -> int:
        
        
        res = 0
        factor = 1
        neg = False

        if x < 0:
            x = x*-1
            neg = True
        num = str(x)


        for i in range(len(num)):
            j = int(num[i])
            res += j * factor
            factor *= 10
            if res >= 2**31 - 1:
                return 0


        if neg == False:
            return res
        else:
            res = res * -1
            return res

        