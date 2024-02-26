# 1442 - Number of Operations to Make Network Connected
# Date: 2022-11-26
# Runtime: 1384 ms, Memory: 34.3 MB
# Submission Id: 849881627


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size
    
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
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        return True
    
        
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        uf = UnionFind(n)
        cables_needed = n-1
        for i, j in connections:
            if uf.union(i, j):
                cables_needed -= 1
        
        return cables_needed