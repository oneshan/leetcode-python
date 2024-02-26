# 0984 - Most Stones Removed with Same Row or Column
# Date: 2022-11-15
# Runtime: 295 ms, Memory: 14.7 MB
# Submission Id: 843932533


from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.root = list(range(size))
        
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:  # already merged
            return 0
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        return 1

    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        union_set = UnionFind(n)
        same_row, same_col = defaultdict(int), defaultdict(int)
        removed = 0
        for idx, (row, col) in enumerate(stones):
            if row not in same_row:
                same_row[row] = idx
            else:
                removed += union_set.union(same_row[row], idx)
            if col not in same_col:
                same_col[col] = idx
            else:
                removed += union_set.union(same_col[col], idx)
        return removed