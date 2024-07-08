# 2139 - Detect Squares
# Date: 2024-05-22
# Runtime: 204 ms, Memory: 18.2 MB
# Submission Id: 1264866496


class DetectSquares:

    def __init__(self):
        self.counter = Counter()
        self.same_x = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.same_x[x].add(y)
        self.counter[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for y2 in self.same_x[x1]:
            if y1 == y2:
                continue
            length = abs(y2-y1)
            for x2 in (x1 + length, x1 - length):
                res += self.counter[(x1, y2)] * self.counter[(x2, y1)] * self.counter[(x2, y2)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)