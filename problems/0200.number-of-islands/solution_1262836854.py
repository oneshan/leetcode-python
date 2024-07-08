# 0200 - Number of Islands
# Date: 2024-05-20
# Runtime: 247 ms, Memory: 22.9 MB
# Submission Id: 1262836854


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size
        self.count = size

    def find(self, x):
        rx = self.root[x]
        if self.root[x] != x:
            self.root[x] = self.find(rx)
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
            self.rank[rx] += self.rank[ry]
        self.count -= 1

    def get_islands(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_r, len_c = len(grid), len(grid[0])

        uf = UnionFind(len_r * len_c)
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == '1':
                    for nr, nc in (r-1, c), (r, c-1):
                        if 0 <= nr < len_r and 0 <= nc < len_c and grid[nr][nc] == '1':
                            uf.union(r * len_c + c, nr * len_c + nc)
                else:
                    uf.count -= 1

        return uf.get_islands()