# 0869 - Similar String Groups
# Date: 2023-04-28
# Runtime: 1997 ms, Memory: 16.7 MB
# Submission Id: 940948755


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [0 for _ in range(n)]
        
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
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        def is_similar(s1, s2):
            return sum(c1 != c2 for c1, c2 in zip(s1, s2)) in (0, 2)
        
        n = len(strs)
        ans = n
        dsu = UnionFind(n)
        for i in range(n):
            for j in range(i):
                if is_similar(strs[i], strs[j]) and dsu.union(i, j):
                    ans -= 1
        return ans