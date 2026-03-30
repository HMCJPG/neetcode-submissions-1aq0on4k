class Solution:
    def addBinary(self, a: str, b: str) -> str:
        

        a_bin = int(a, 2)
        b_bin = int(b, 2)

        total = a_bin + b_bin

        return format(total, 'b')