# 2505 - Number of Good Paths
# Date: 2023-01-15
# Runtime: 2396 ms, Memory: 36.6 MB
# Submission Id: 878620420


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
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.rank[rx] += 1
            self.root[ry] = rx
        return True
    

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        uf = UnionFind(n)
        
        max_val_edges = defaultdict(list)
        for a, b in edges:
            max_val = max(vals[a], vals[b])
            max_val_edges[max_val].append((a, b))
        
        val_to_nodes = defaultdict(list)
        for idx, val in enumerate(vals):
            val_to_nodes[val].append(idx)
            
        ans = n
        for val, nodes in sorted(val_to_nodes.items()):
            for a, b in max_val_edges[val]:
                uf.union(a, b)
            count = Counter(uf.find(x) for x in nodes)
            for c in count.values():
                ans += c * (c-1) // 2
        return ans

        