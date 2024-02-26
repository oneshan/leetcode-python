# 2403 - Count Unreachable Pairs of Nodes in an Undirected Graph
# Date: 2023-03-25
# Runtime: 2234 ms, Memory: 73.6 MB
# Submission Id: 921619497


from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [0] * n
        
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
        

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:        
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        
        group = defaultdict(int)
        for i in range(n):
            group[uf.find(i)] += 1
        
        ans, remains = 0, n
        for gid, count in group.items():
            remains -= count
            ans += count * remains
        return ans