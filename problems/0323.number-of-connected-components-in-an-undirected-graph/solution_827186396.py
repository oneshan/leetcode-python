# 0323 - Number of Connected Components in an Undirected Graph
# Date: 2022-10-21
# Runtime: 244 ms, Memory: 15.5 MB
# Submission Id: 827186396


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        
    def find(self, x):
        if x == self.root[x]:
            return x
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
            self.rank[root_x] += 1
            self.root[root_y] = root_x
        return True
    
    def get_count(self):
        return sum(x == self.root[x] for x in range(self.size))
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for p, q in edges:
            uf.union(p, q)
        return uf.get_count()