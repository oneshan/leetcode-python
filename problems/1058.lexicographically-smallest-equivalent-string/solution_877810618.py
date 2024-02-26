# 1058 - Lexicographically Smallest Equivalent String
# Date: 2023-01-14
# Runtime: 44 ms, Memory: 13.8 MB
# Submission Id: 877810618


class UnionFind:
    def __init__(self):
        self.root = list(range(26))
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if rx < ry:
            self.root[ry] = rx
        else:
            self.root[rx] = ry
        return True

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        
        for c1, c2 in zip(s1, s2):
            x = ord(c1)-ord('a')
            y = ord(c2)-ord('a')
            uf.union(x, y)
            
        def convert(ch):
            idx = ord(ch)-ord('a')
            new_idx = uf.find(idx)
            return chr(new_idx + ord('a'))
            
        return ''.join([convert(ch) for ch in baseStr])