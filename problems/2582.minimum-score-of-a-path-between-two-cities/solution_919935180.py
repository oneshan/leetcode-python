# 2582 - Minimum Score of a Path Between Two Cities
# Date: 2023-03-22
# Runtime: 1792 ms, Memory: 58.8 MB
# Submission Id: 919935180


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0 for _ in range(size)]
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        else:
            self.rank[root_x] += 1
            self.root[root_y] = root_x
    
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dsu = UnionFind(n+1)
        ans = float('inf')
        
        for x, y, w in roads:
            dsu.union(x, y)
            
        for x, y, w in roads:
            if dsu.find(1) == dsu.find(x):
                ans = min(ans, w)
        return ans