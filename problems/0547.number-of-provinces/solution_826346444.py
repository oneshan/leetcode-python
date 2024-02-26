# 0547 - Number of Provinces
# Date: 2022-10-20
# Runtime: 395 ms, Memory: 14.3 MB
# Submission Id: 826346444


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for x in range(n):
            for y in range(n):
                if isConnected[x][y]:
                    uf.union(x,y)
        return sum(x == uf.find(x) for x in range(n))