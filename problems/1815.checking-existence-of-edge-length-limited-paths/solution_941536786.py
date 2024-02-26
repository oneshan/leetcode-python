# 1815 - Checking Existence of Edge Length Limited Paths
# Date: 2023-04-29
# Runtime: 1915 ms, Memory: 62.4 MB
# Submission Id: 941536786


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
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
        return True
        
        
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = UnionFind(n)
        len_q = len(queries)
        len_e = len(edgeList)
        ans = [False] * len_q
        
        queries = [(limit, x, y, idx) for idx, (x, y, limit) in enumerate(queries)]
        queries.sort()
        edgeList.sort(key=lambda x: x[2])
        
        edge_idx = 0
        for limit, x, y, idx in queries:
            while edge_idx < len_e and edgeList[edge_idx][2] < limit:
                n1, n2, _ = edgeList[edge_idx]
                dsu.union(n1, n2)
                edge_idx += 1
            ans[idx] = dsu.find(x) == dsu.find(y)
        return ans