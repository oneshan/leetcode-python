# 2121 - Find if Path Exists in Graph
# Date: 2024-04-21
# Runtime: 1433 ms, Memory: 107.4 MB
# Submission Id: 1237945590


class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.root = list(range(size))

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
        return True

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        
        return uf.find(source) == uf.find(destination)