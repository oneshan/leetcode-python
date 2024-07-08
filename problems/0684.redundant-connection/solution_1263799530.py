# 0684 - Redundant Connection
# Date: 2024-05-21
# Runtime: 54 ms, Memory: 17 MB
# Submission Id: 1263799530


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] >= self.rank[ry]:
            self.rank[rx] += self.rank[ry]
            self.root[ry] = rx
        else:
            self.rank[ry] += self.rank[rx]
            self.root[rx] = ry
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n+1)
        for a, b in edges:
            if not uf.union(a, b):
                return [a, b]