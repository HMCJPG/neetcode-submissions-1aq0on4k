class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res = 1

        if n == 0:
            return 1

        

        elif n > 0:
            for i in range(n):
                res *= x
        
        else:
            n = -n
            print(n)
            for i in range(n):
                res *= x

            res = 1 / res



        

        return res