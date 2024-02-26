# 2139 - Detect Squares
# Date: 2022-10-17
# Runtime: 272 ms, Memory: 15.9 MB
# Submission Id: 824451000


from collections import defaultdict, Counter

class DetectSquares:

    def __init__(self):
        self.table = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.table[x][y] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point
        for y2 in self.table[x1]:
            if y1 == y2:
                continue
            ans += self.table[x1][y2] * self.table[x1+(y1-y2)][y1] * self.table[x1+(y1-y2)][y2]
            ans += self.table[x1][y2] * self.table[x1+(y2-y1)][y1] * self.table[x1+(y2-y1)][y2]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)