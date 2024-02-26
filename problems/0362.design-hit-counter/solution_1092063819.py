# 0362 - Design Hit Counter
# Date: 2023-11-05
# Runtime: 36 ms, Memory: 16.3 MB
# Submission Id: 1092063819


from collections import deque

class HitCounter:

    def __init__(self):
        self.record = deque()
        self.counter = 0

    def hit(self, timestamp: int) -> None:
        self.record.append(timestamp)
        self.counter += 1
        

    def getHits(self, timestamp: int) -> int:
        while self.record and timestamp - self.record[0] >= 300:
            self.record.popleft()
            self.counter -= 1
        return self.counter


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)