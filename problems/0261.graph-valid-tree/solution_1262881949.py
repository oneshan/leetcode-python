# 0261 - Graph Valid Tree
# Date: 2024-05-20
# Runtime: 82 ms, Memory: 18.3 MB
# Submission Id: 1262881949


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size
        self.groups = size

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
            
        self.groups -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False
        return uf.groups == 1