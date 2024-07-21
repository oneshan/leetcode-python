# 1711 - Find Valid Matrix Given Row and Column Sums
# Date: 2024-07-20
# Runtime: 575 ms, Memory: 21.8 MB
# Submission Id: 1326834204


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        len_r = len(rowSum)
        len_c = len(colSum)

        res = [[0] * len_c for _ in range(len_r)]
        for r in range(len_r):
            for c in range(len_c):
                res[r][c] = min(rowSum[r], colSum[c])
                rowSum[r] -= res[r][c]
                colSum[c] -= res[r][c]

        return res