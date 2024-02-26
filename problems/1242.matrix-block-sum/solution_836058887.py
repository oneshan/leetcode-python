# 1242 - Matrix Block Sum
# Date: 2022-11-03
# Runtime: 297 ms, Memory: 15.1 MB
# Submission Id: 836058887


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        len_r, len_c = len(mat), len(mat[0])
        block_sum = [[0] * len_c for _ in range(len_r)]
        
        for r in range(len_r):
            row_sum = 0
            for c in range(len_c):
                row_sum += mat[r][c]
                block_sum[r][c] = row_sum
                if r > 0:
                    block_sum[r][c] += block_sum[r-1][c]
        
        ans = [[0] * len_c for _ in range(len_r)]
        for r in range(len_r):
            for c in range(len_c):
                min_r = max(0, r-k)
                min_c = max(0, c-k)
                max_r = min(len_r-1, r+k)
                max_c = min(len_c-1, c+k)
                
                ans[r][c] = block_sum[max_r][max_c]
                if min_r > 0:
                    ans[r][c] -= block_sum[min_r-1][max_c]
                if min_c > 0:
                    ans[r][c] -= block_sum[max_r][min_c-1]
                if min_r > 0 and min_c > 0:
                    ans[r][c] += block_sum[min_r-1][min_c-1]

        return ans