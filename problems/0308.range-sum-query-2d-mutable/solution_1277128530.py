# 0308 - Range Sum Query 2D - Mutable
# Date: 2024-06-04
# Runtime: 168 ms, Memory: 18.2 MB
# Submission Id: 1277128530


class BITTree:
    def __init__(self, matrix):
        self.len_r = len(matrix)
        self.len_c = len(matrix[0])
        self.bits = [[0] * (self.len_c+1) for _ in range(self.len_r+1)]
        for r in range(self.len_r):
            for c in range(self.len_c):
                self.update(r, c, matrix[r][c])

    def update(self, row, col, val):
        r = row + 1
        while r <= self.len_r:
            c = col + 1
            while c <= self.len_c:
                self.bits[r][c] += val
                c += c & -c
            r += r & -r

    def get_sum(self, row, col):
        res = 0
        r = row + 1
        while r > 0:
            c = col + 1
            while c > 0:
                res += self.bits[r][c]
                c -= c & -c
            r -= r & -r
        return res


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.tree = BITTree(matrix)

    def update(self, row: int, col: int, val: int) -> None:
        self.tree.update(row, col, val - self.matrix[row][col])
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.tree.get_sum(row2, col2)
                + self.tree.get_sum(row1-1, col1-1)
                - self.tree.get_sum(row1-1, col2)
                - self.tree.get_sum(row2, col1-1))

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)