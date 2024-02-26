# 2297 - Amount of New Area Painted Each Day
# Date: 2022-11-19
# Runtime: 5702 ms, Memory: 58.7 MB
# Submission Id: 846332861


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size
        self.end = list(range(size))
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
    
        self.rank[root_x] += 1
        self.root[root_y] = root_x
        self.end[root_x] = max(self.end[root_x], self.end[root_y])
        return True
    
    def max_end(self, x):
        root_x = self.find(x)
        return self.end[root_x]

    
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        painted = UnionFind(50001)
        
        ans = [0] * len(paint)
        for idx, (start, end) in enumerate(paint):
            count = 0
            curr = painted.max_end(start)
            while curr < end:
                painted.union(curr, curr+1)
                count += 1
                curr = painted.max_end(curr)
            ans[idx] = count
        return ans