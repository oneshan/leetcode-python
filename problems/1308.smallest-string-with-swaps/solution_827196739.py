# 1308 - Smallest String With Swaps
# Date: 2022-10-21
# Runtime: 1856 ms, Memory: 50.3 MB
# Submission Id: 827196739


from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        
    def find(self, x):
        if x == self.root[x]:
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
            self.rank[root_x] += 1
            self.root[root_y] = root_x
    
    def get_groups(self):
        groups = defaultdict(list)
        for i in range(self.size):
            groups[self.find(i)].append(i)
        return groups.values()
    
        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for i, j in pairs:
            uf.union(i, j)
        
        ans = list(s)
        for idxs in uf.get_groups():
            substr = [s[i] for i in idxs]
            for new_i, new_ch in zip(idxs, sorted(substr)):
                ans[new_i] = new_ch
        return ''.join(ans)