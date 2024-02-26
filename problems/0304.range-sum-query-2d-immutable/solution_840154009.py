# 0304 - Range Sum Query 2D - Immutable
# Date: 2022-11-09
# Runtime: 1841 ms, Memory: 24.8 MB
# Submission Id: 840154009


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        
        len_r, len_c = len(matrix), len(matrix[0])
        self.dp = [[0] * (len_c+1) for _ in range(len_r+1)]
        for r in range(len_r):
            for c in range(len_c):
                self.dp[r+1][c+1] = (matrix[r][c]
                                     + self.dp[r+1][c]
                                     + self.dp[r][c+1]
                                     - self.dp[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.dp[row2+1][col2+1]
                - self.dp[row1][col2+1]
                - self.dp[row2+1][col1]
                + self.dp[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)