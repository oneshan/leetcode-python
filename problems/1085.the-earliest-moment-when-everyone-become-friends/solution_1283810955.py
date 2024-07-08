# 1085 - The Earliest Moment When Everyone Become Friends
# Date: 2024-06-10
# Runtime: 94 ms, Memory: 17 MB
# Submission Id: 1283810955


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] >= self.rank[ry]:
            self.root[ry] = rx
            self.rank[rx] += self.rank[ry]
        else:
            self.root[rx] = ry
            self.rank[ry] += self.rank[rx]
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs.sort()
        for ts, a, b in logs:
            if uf.union(a, b):
                n -= 1
                if n == 1:
                    return ts
        return -1