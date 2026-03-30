class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = ["+", "-", "*", "/"]
        nums = []

        for token in tokens:
            if token not in ops:
                nums.append(int(token))
            else:
                valB = nums.pop()
                valA = nums.pop()

                if token == "+":
                    val = valA + valB

                elif token == "-":
                    val = valA - valB

                elif token == "*":
                    val = valA * valB

                else:
                    val = math.trunc(valA / valB)

                nums.append(val)

        return nums.pop()
    