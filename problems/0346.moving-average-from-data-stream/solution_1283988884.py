# 0346 - Moving Average from Data Stream
# Date: 2024-06-11
# Runtime: 53 ms, Memory: 19.6 MB
# Submission Id: 1283988884


class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        return self.total / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)