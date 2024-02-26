# 1463 - The K Weakest Rows in a Matrix
# Date: 2023-09-18
# Runtime: 106 ms, Memory: 16.8 MB
# Submission Id: 1052242099


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sum_mat = [(idx, sum(m)) for idx, m in enumerate(mat)]
        sum_mat.sort(key=lambda x: x[1])
        return [sum_mat[i][0] for i in range(k)]