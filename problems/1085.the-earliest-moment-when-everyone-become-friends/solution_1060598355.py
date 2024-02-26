# 1085 - The Earliest Moment When Everyone Become Friends
# Date: 2023-09-27
# Runtime: 103 ms, Memory: 16.6 MB
# Submission Id: 1060598355


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        self.components = size
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.rank[root_x] += 1
            self.root[root_y] = root_x
        self.components -= 1

    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n)
        for ts, p, q in logs:
            uf.union(p, q)
            if uf.components == 1:
                return ts
        return -1