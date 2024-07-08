# 0936 - RLE Iterator
# Date: 2024-06-20
# Runtime: 35 ms, Memory: 17.1 MB
# Submission Id: 1294589512


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.idx = 0
        self.size = len(encoding)

    def next(self, n: int) -> int:
        res = -1
        while n and self.idx+1 < self.size:
            res = self.encoding[self.idx+1]
            if n >= self.encoding[self.idx]:
                n -= self.encoding[self.idx]
                self.idx += 2
            else:
                self.encoding[self.idx] -= n
                n = 0
                
        return res if n == 0 else -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)