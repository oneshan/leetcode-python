# 0261 - Graph Valid Tree
# Date: 2022-10-21
# Runtime: 193 ms, Memory: 15.4 MB
# Submission Id: 827184321


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
        if root_x == root_y:  # circle here
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:  # merge
            self.rank[root_x] +=1
            self.root[root_y] = root_x
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        uf = UnionFind(n)
        for p, q in edges:
            connected = uf.union(p, q)
            if not connected:
                return False
        return True