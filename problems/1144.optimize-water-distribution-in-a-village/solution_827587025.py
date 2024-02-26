# 1144 - Optimize Water Distribution in a Village
# Date: 2022-10-22
# Runtime: 1402 ms, Memory: 20.2 MB
# Submission Id: 827587025


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
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        return True
    
        
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edges = []
        for idx, weight in enumerate(wells, 1):
            edges.append([weight, 0, idx])
        for p, q, weight in pipes:
            edges.append([weight, p, q])
            
        edges.sort()
        uf = UnionFind(n+1)
        total_cost = 0
        for weight, p, q in edges:
            if uf.union(p, q):
                total_cost += weight
        return total_cost