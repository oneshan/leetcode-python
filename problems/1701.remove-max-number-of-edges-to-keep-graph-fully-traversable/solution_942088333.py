# 1701 - Remove Max Number of Edges to Keep Graph Fully Traversable
# Date: 2023-04-30
# Runtime: 2206 ms, Memory: 56.5 MB
# Submission Id: 942088333


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n+1))
        self.rank = [0] * (n+1)
        self.size = n
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return 0
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
        self.size -= 1
        return 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        required = 0
        
        for t, x, y in edges:
            if t == 3:
                required += max(alice.union(x, y), bob.union(x, y))
        
        for t, x, y in edges:
            if t == 1:
                required += alice.union(x, y)
            elif t == 2:
                required += bob.union(x, y)
        
        if alice.size == bob.size == 1:
            return len(edges) - required
        return -1