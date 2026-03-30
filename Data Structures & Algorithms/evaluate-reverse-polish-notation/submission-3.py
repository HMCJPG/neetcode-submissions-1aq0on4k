class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        ops = []
        ops.append("+")
        ops.append("-")
        ops.append("*")
        ops.append("/")

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    c = a + b
                    stack.append(c)
                elif token == "-":
                    c = a - b
                    stack.append(c)
                elif token == "*":
                    c = a * b
                    stack.append(c)
                elif token == "/":
                    c = int(a / b)
                    stack.append(c)

        if stack:
            return stack[-1]

