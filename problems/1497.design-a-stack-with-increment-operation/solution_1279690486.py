# 1497 - Design a Stack With Increment Operation
# Date: 2024-06-07
# Runtime: 61 ms, Memory: 17.4 MB
# Submission Id: 1279690486


class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append([x, 0])

    def pop(self) -> int:
        if not self.stack:
            return -1
        num, inc = self.stack.pop()
        if self.stack:
            self.stack[-1][1] += inc
        return num + inc

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.stack[min(k, len(self.stack))-1][1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)