class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = None

    def updateMinimum(self) -> None:
        if len(self.stack) > 0:
            self.minimum = sorted(self.stack)[0]
        else:
            self.minimum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.updateMinimum()

    def pop(self) -> None:
        self.stack.pop()
        self.updateMinimum()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()