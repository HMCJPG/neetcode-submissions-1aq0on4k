class FreqStack:

    def __init__(self):
        self.valCounts = {}
        self.freqCounts = {}
        self.max_freq = 0 
        

    def push(self, val: int) -> None:
        f = self.valCounts.get(val, 0) + 1
        self.valCounts[val] = f

        if f > self.max_freq:
            self.max_freq = f

        if f not in self.freqCounts:
            self.freqCounts[f] = []
        self.freqCounts[f].append(val)

    def pop(self) -> int:

        val = self.freqCounts[self.max_freq].pop()
        self.valCounts[val] -= 1

        if not self.freqCounts[self.max_freq]:
            self.max_freq -= 1


        return val        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()