# 1903 - Design Most Recently Used Queue
# Date: 2024-05-27
# Runtime: 172 ms, Memory: 18.5 MB
# Submission Id: 1269421450


from sortedcontainers import SortedList

class MRUQueue:

    def __init__(self, n: int):
        self.sl = SortedList((i, i) for i in range(1, n+1))  # (ts, val)
        self.clock = 1 + n

    def fetch(self, k: int) -> int:
        _, val = self.sl.pop(k-1)
        self.sl.add((self.clock, val))
        self.clock += 1
        return val


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)