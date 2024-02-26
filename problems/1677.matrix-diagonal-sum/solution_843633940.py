# 1677 - Matrix Diagonal Sum
# Date: 2022-11-15
# Runtime: 258 ms, Memory: 14.2 MB
# Submission Id: 843633940


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            if i != n-1-i:
                ans += mat[i][-1-i]
        return ans