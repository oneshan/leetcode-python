# 0695 - Max Area of Island
# Date: 2024-05-20
# Runtime: 111 ms, Memory: 16.8 MB
# Submission Id: 1262845794


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] >= self.rank[ry]:
            self.rank[rx] += self.rank[ry]
            self.root[ry] = self.root[rx]
        else:
            self.rank[ry] += self.rank[rx]
            self.root[rx] = self.root[ry]

    def get_max_area(self):
        return max(self.rank)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        uf = UnionFind(len_r * len_c)
        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c]:
                    for nr, nc in (r-1, c), (r, c-1):
                        if 0 <= nr < len_r and 0 <= nc < len_c and grid[nr][nc]:
                            uf.union(r * len_c + c, nr * len_c + nc)
                else:
                    uf.rank[r * len_c + c] = 0
        return uf.get_max_area()