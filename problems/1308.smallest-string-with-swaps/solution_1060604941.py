# 1308 - Smallest String With Swaps
# Date: 2023-09-27
# Runtime: 542 ms, Memory: 52.7 MB
# Submission Id: 1060604941


from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        self.size = size
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
            
    def get_group(self):
        group = defaultdict(list)
        for i in range(self.size):
            group[self.find(i)].append(i)
        return group

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for a, b in pairs:
            uf.union(a, b)    
        
        ans = [None] * n
        group = uf.get_group()
        for idxs in group.values():
            for idx, ch in zip(idxs, sorted(s[i] for i in idxs)):
                ans[idx] = ch
        return ''.join(ans)