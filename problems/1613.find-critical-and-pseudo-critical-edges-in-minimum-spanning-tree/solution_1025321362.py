# 1613 - Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
# Date: 2023-08-19
# Runtime: 1120 ms, Memory: 16.6 MB
# Submission Id: 1025321362


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
        self.max_size = 1
    
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.root[ry] = rx
        self.rank[rx] += self.rank[ry]
        self.max_size = max(self.max_size, self.rank[rx])
        return True
    

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        new_edges = [(weight, u, v, idx) for idx, (u, v, weight) in enumerate(edges)]
        new_edges.sort()
        
        union_find = UnionFind(n)
        mst_w = 0
        for w, u, v, _ in new_edges:
            if union_find.union(u, v):
                mst_w += w
        
        critical = []
        pseudo_critical = []
        for w, u, v, i in new_edges:
            
            # Ignore the edge_i and calculate MST weight
            uf_ignore = UnionFind(n)
            ignore_w = 0
            for w_ignore, x, y, j in new_edges:
                if i != j and uf_ignore.union(x, y):
                    ignore_w += w_ignore

            # If the graph is disconnected or the total weight is greater,
            # the edge is critical
            if uf_ignore.max_size < n or ignore_w > mst_w:
                critical.append(i)
                continue

            # Force this edge and calculate MST weight
            uf_force = UnionFind(n)
            force_w = w
            uf_force.union(u, v)
            for w_force, x, y, j in new_edges:
                if i != j and uf_force.union(x, y):
                    force_w += w_force

            # If total weight is the same, the edge is pseudo-critical
            if force_w == mst_w:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]