class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        scale = 1
        integer = 0
        n = len(digits) - 1
        res = []

        for i in range(n, -1, -1):

            integer += digits[i] * scale
            scale = scale * 10

        integer += 1

        int_str = str(integer)

        for digit in int_str:

            res.append(int(digit))

        return res
        



