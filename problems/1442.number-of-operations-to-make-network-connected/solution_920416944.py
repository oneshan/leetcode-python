# 1442 - Number of Operations to Make Network Connected
# Date: 2023-03-23
# Runtime: 491 ms, Memory: 33.9 MB
# Submission Id: 920416944


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [0 for _ in range(n)]
    
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
        elif self.rank[ry] > self.rank[rx]:
            self.root[rx] = ry
        else:
            self.rank[rx] += 1
            self.root[ry] = rx
        return True
    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        uf = UnionFind(n)
        count = 0
        for x, y in connections:
            if uf.union(x, y):
                count += 1
        return n - count - 1