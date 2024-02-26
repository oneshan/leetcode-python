# 0801 - Is Graph Bipartite?
# Date: 2022-12-02
# Runtime: 217 ms, Memory: 14.5 MB
# Submission Id: 853416214


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        return True
    
    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        uf = UnionFind(n)
        
        for node in range(n):
            for neighbor in graph[node]:
                if uf.find(node) == uf.find(neighbor):
                    return False
                uf.union(graph[node][0], neighbor)
        return True