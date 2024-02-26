# 0232 - Implement Queue using Stacks
# Date: 2024-01-29
# Runtime: 25 ms, Memory: 16.6 MB
# Submission Id: 1159775863


class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        if self.out_stack:
            return self.out_stack[-1]
        return self.in_stack[0]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()