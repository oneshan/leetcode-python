# 1085 - The Earliest Moment When Everyone Become Friends
# Date: 2022-10-20
# Runtime: 137 ms, Memory: 14.4 MB
# Submission Id: 826398816


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        
    def find(self, x):
        if x == self.root[x]:
            return self.root[x]
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] == self.rank[root_y]:
                self.root[root_y] = self.root[root_x]
                self.rank[root_x] += 1
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = self.root[root_x]
            else:
                self.root[root_x] = self.root[root_y]

    @property
    def count(self):
        return sum(x == self.root[x] for x in range(self.size))
        
        
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs.sort()
        for date, x, y in logs:
            uf.union(x,y)
            if uf.count == 1:
                return date
        return -1