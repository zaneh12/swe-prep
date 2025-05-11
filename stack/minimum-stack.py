
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
if __name__ == "__main__":
    s = MinStack()
    s.push(3)
    s.push(5)
    print("Min:", s.getMin())  # 3
    s.push(2)
    s.push(1)
    print("Min:", s.getMin())  # 1
    s.pop()
    print("Top:", s.top())     # 2
    print("Min:", s.getMin())  # 2
