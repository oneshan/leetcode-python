# 1677 - Matrix Diagonal Sum
# Date: 2022-11-15
# Runtime: 276 ms, Memory: 14.1 MB
# Submission Id: 843635741


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][-1-i]
        if n & 1:
            ans -= mat[n>>1][n>>1]
        return ans