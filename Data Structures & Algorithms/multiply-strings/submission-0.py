class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        n1 = len(num1) - 1
        n2 = len(num2) - 1

        n1Parse = 0
        n2Parse = 0


        scale_factor = 1
        for i in range(n1, -1, -1):
            n1Parse += int(num1[i]) * scale_factor
            scale_factor = scale_factor * 10

        scale_factor = 1
        for i in range(n2, -1, -1):
            n2Parse += int(num2[i]) * scale_factor
            scale_factor = scale_factor * 10

        res = str(n1Parse * n2Parse)
        print(n1Parse)
        print(n2Parse)
        print(res)

        return res



        