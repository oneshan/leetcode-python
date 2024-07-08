# 2139 - Detect Squares
# Date: 2024-05-22
# Runtime: 243 ms, Memory: 18.3 MB
# Submission Id: 1264934324


class DetectSquares:

    def __init__(self):
        self.counter = Counter()

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for x2, y2 in self.counter:
            if x1 == x2 or y1 == y2 or abs(x1-x2) != abs(y1-y2):
                continue
            res += self.counter[(x1, y2)] * self.counter[(x2, y1)] * self.counter[(x2, y2)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)