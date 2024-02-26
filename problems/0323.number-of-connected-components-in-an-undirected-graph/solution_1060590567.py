# 0323 - Number of Connected Components in an Undirected Graph
# Date: 2023-09-27
# Runtime: 90 ms, Memory: 17.7 MB
# Submission Id: 1060590567


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size
        self.components = size
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
            
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
        self.components -= 1
        
    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
            
        return uf.components