# 1677 - Matrix Diagonal Sum
# Date: 2023-05-08
# Runtime: 135 ms, Memory: 16.7 MB
# Submission Id: 946375760


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n-1-i]
        if n & 1:
            ans -= mat[n>>1][n>>1]
        return ans