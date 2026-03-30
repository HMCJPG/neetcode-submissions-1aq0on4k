class Solution:
    def calPoints(self, operations: List[str]) -> int:
        

        ops = ["+", "C", "D"]
        score = 0
        stack = []


        for op in operations:

            if op not in ops:
                stack.append(op)
                print(stack)

            elif op == "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                num3 = num1 + num2

                stack.append(num2)
                stack.append(num1)
                stack.append(num3)
                print(stack)

            elif op == "C":
                stack.pop()
                print(stack)

            elif op == "D":
                num1 = int(stack.pop())
                num2 = num1 * 2

                stack.append(num1)
                stack.append(num2)
                print(stack)
        
        for item in stack:
            score += int(item)

        return score


