import math

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        res = []

        for i, ast in enumerate(asteroids):

        # Scenario 1: Positive asteroid 
            if ast > 0:
                stack.append(ast)

        # Scenario 2: Negative asteroid, empty stack
            elif not stack and ast < 0:
                res.append(ast)

        # Scenario 3: Negative asteroid, stack has items
            elif ast < 0 and stack:
                while stack and stack[-1] < math.fabs(ast):
                    stack.pop()
                if stack and stack[-1] == math.fabs(ast):
                    stack.pop()
                elif not stack:
                    res.append(ast)


        flipStack = []
        while stack:
            flipStack.append(stack.pop())

        while flipStack:
            res.append(flipStack.pop())

        return res
