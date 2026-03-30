class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minStack.append(float('inf'))

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if val <= self.minStack[-1]:
                self.minStack.append(val)

    def pop(self) -> None:
        topElement = self.stack.pop()
        if self.minStack and topElement == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]
