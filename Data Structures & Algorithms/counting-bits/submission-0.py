class Solution:
    def countBits(self, n: int) -> List[int]:
        

        count = 0
        res = [0] * (n + 1)


        for i in range(n + 1):

            num = i
            count = 0

            while num:
                count += num & 1
                num >>= 1

            res[i] = count

        return res
                
            
            

