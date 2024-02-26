# 0937 - Online Stock Span
# Date: 2022-12-08
# Runtime: 440 ms, Memory: 19.3 MB
# Submission Id: 856696366


class StockSpanner:

    def __init__(self):
        self.stack = [(float('inf'), 0)]
        self.index = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.index += 1
        val = self.index - self.stack[-1][1]
        self.stack.append((price, self.index))
        return val


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)