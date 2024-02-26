# 2101 - Last Day Where You Can Still Cross
# Date: 2023-06-30
# Runtime: 1497 ms, Memory: 25.3 MB
# Submission Id: 982999770


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.size[rx] > self.size[ry]:
            rx, ry = ry, rx
        self.root[rx] = ry
        self.size[ry] += self.size[rx]
        

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        uf = UnionFind(row * col + 2)
        grid = [[0] * col for _ in range(row)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for i in range(row * col):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 1
            idx_1 = r * col + c + 1
            for dr, dc in dirs:
                next_r, next_c = r + dr, c + dc
                idx_2 = next_r * col + next_c + 1
                if 0 <= next_r < row and 0 <= next_c < col and grid[next_r][next_c] == 1:
                    uf.union(idx_1, idx_2)
            
            if c == 0:
                uf.union(0, idx_1)
            if c == col - 1:
                uf.union(row * col + 1, idx_1)
            if uf.find(0) == uf.find(row * col + 1):
                return i