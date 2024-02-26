# 0346 - Moving Average from Data Stream
# Date: 2022-07-19
# Runtime: 113 ms, Memory: 17.2 MB
# Submission Id: 751148535


from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.sum = 0
        
    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            prev = self.queue.popleft()
            self.sum -= prev
        self.sum += val
        self.queue.append(val)
        return self.sum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)