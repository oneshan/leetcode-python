# 1711 - Find Valid Matrix Given Row and Column Sums
# Date: 2024-07-20
# Runtime: 366 ms, Memory: 21.8 MB
# Submission Id: 1326840937


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        len_r = len(rowSum)
        len_c = len(colSum)

        res = [[0] * len_c for _ in range(len_r)]
        r = c = 0
        while r < len_r and c < len_c:
            res[r][c] = min(rowSum[r], colSum[c])
            rowSum[r] -= res[r][c]
            colSum[c] -= res[r][c]
            if rowSum[r] == colSum[c]:
                r += 1
                c += 1
            elif rowSum[r] > colSum[c]:
                c += 1
            else:
                r += 1

        return res