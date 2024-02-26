# 0937 - Online Stock Span
# Date: 2023-09-13
# Runtime: 341 ms, Memory: 21.6 MB
# Submission Id: 1048448688


class StockSpanner:

    def __init__(self):
        self.stack = [(float('inf'), 0)]
        self.index = 0

    def next(self, price: int) -> int:
        self.index += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        val = self.index - self.stack[-1][1]
        self.stack.append((price, self.index))
        return val


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)