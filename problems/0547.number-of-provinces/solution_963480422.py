# 0547 - Number of Provinces
# Date: 2023-06-04
# Runtime: 203 ms, Memory: 16.6 MB
# Submission Id: 963480422


class UnionFind:
    def __init__(self, n):
        self.rank = [0] * n
        self.root = list(range(n))
    
    def find(self, x):
        root_x = self.root[x]
        if root_x == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        
        ans = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    ans -= uf.union(i, j)
        return ans