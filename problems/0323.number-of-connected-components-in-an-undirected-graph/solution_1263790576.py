# 0323 - Number of Connected Components in an Undirected Graph
# Date: 2024-05-21
# Runtime: 96 ms, Memory: 18.2 MB
# Submission Id: 1263790576


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
        self.groups = n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] >= self.rank[ry]:
            self.root[ry] = rx
            self.rank[rx] += self.rank[ry]
        else:
            self.root[rx] = ry
            self.rank[ry] += self.rank[rx]
        
        self.groups -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.groups