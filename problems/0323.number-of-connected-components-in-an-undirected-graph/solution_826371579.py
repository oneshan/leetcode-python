# 0323 - Number of Connected Components in an Undirected Graph
# Date: 2022-10-20
# Runtime: 240 ms, Memory: 15.4 MB
# Submission Id: 826371579


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = self.root[root_x]
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = self.root[root_y]
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
            
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        return sum(x == uf.root[x] for x in range(n))