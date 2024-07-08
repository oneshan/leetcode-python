# 0200 - Number of Islands
# Date: 2024-05-20
# Runtime: 275 ms, Memory: 23.4 MB
# Submission Id: 1262834814


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.root = list(range(size))
        self.rank = [0 for _ in range(size)]

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

    def get_islands(self):
        islands = set()
        for i in range(self.size):
            if self.root[i] == -1:
                continue
            islands.add(self.find(self.root[i]))
        return len(islands)


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
                    uf.root[r * len_c + c] = -1

        return uf.get_islands()