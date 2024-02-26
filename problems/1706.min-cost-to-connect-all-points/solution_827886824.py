# 1706 - Min Cost to Connect All Points
# Date: 2022-10-22
# Runtime: 3137 ms, Memory: 81.6 MB
# Submission Id: 827886824


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
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.rank[root_x] += 1
            self.root[root_y] = self.root[root_x]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = [(abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]), i, j)
                 for i in range(n) for j in range(i+1, n)]
        edges.sort()
        
        uf = UnionFind(n)
        cost = 0
        for weight, p, q in edges:
            if uf.union(p, q):
                cost += weight
        return cost
        
        