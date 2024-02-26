# 0801 - Is Graph Bipartite?
# Date: 2023-05-19
# Runtime: 203 ms, Memory: 16.8 MB
# Submission Id: 953072164


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.root[x], self.root[y]
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
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        uf = UnionFind(n)
        
        for i in range(n):
            for neighbor in graph[i]:
                if uf.find(i) == uf.find(neighbor):
                    return False
                uf.union(graph[i][0], neighbor)
        return True