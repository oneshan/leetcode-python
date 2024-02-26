# 0399 - Evaluate Division
# Date: 2023-05-20
# Runtime: 48 ms, Memory: 16.5 MB
# Submission Id: 953673028


class UnionFind():
    def __init__(self):
        self.root = {}
        self.rank = {}
        
    def find(self, x):
        if x not in self.root:
            self.root[x] = (x, 1)
            self.rank[x] = 1
        if x == self.root[x][0]:
            return self.root[x]
        root_x, rx_by_root = self.find(self.root[x][0])
        self.root[x] = (root_x, self.root[x][1] * rx_by_root)
        return self.root[x]
    
    def union(self, x, y, val):
        root_x, x_by_root = self.find(x)
        root_y, y_by_root = self.find(y)
        if root_x == root_y:
            return
        
        # (x/root_x / y/root_y / x/y) = root_y / root_x
        multp = x_by_root / y_by_root / val
        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = (root_y, 1/multp)
        else:
            self.root[root_y] = (root_x, multp)
            self.rank[root_x] += 1

            
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for (a, b), value in zip(equations, values):
            uf.union(a, b, value)
            
        ans = [-1] * len(queries)
        for idx, (a, b) in enumerate(queries):
            if a in uf.root and b in uf.root:
                root_a, a_by_root = uf.find(a)
                root_b, b_by_root = uf.find(b)
                if root_a == root_b:
                    ans[idx] = a_by_root / b_by_root
        return ans