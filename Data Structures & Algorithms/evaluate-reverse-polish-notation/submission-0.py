class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        numStack = []
        listOps = []
        listOps.append("+")
        listOps.append("-")
        listOps.append("*")
        listOps.append("/")


        for token in tokens:
            if token not in listOps:
                numStack.append(int(token))
            else:
                b = numStack.pop()
                a = numStack.pop()

                if token == "+":
                    c = a + b
                    numStack.append(c)
                elif token == "-":
                    c = a - b
                    numStack.append(c)                    
                elif token == "*":
                    c = a * b
                    numStack.append(c)                    
                elif token == "/":   
                    c = int(a / b)
                    numStack.append(c)

        return numStack[-1]                     