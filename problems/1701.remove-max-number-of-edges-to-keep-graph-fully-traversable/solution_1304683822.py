# 1701 - Remove Max Number of Edges to Keep Graph Fully Traversable
# Date: 2024-06-30
# Runtime: 1631 ms, Memory: 56.3 MB
# Submission Id: 1304683822


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
        self.groups = n
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        self.groups -= 1
        if self.rank[rx] >= self.rank[ry]:
            self.root[ry] = rx
            self.rank[rx] += self.rank[ry]
        else:
            self.root[rx] = ry
            self.rank[ry] += self.rank[rx]
        return True
    
    def is_fully_connected(self):
        return self.groups == 2


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        alice_uf = UnionFind(n+1)
        bob_uf = UnionFind(n+1)

        required = 0
        for e_type, a, b in edges:
            if e_type == 3:
                required += alice_uf.union(a, b) | bob_uf.union(a, b)

        for e_type, a, b in edges:
            if e_type == 1:
                required += alice_uf.union(a, b)
            if e_type == 2:
                required += bob_uf.union(a, b)

        if alice_uf.is_fully_connected() and bob_uf.is_fully_connected():
            return len(edges) - required
        return -1