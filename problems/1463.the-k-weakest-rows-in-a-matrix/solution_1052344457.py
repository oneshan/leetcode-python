# 1463 - The K Weakest Rows in a Matrix
# Date: 2023-09-18
# Runtime: 105 ms, Memory: 16.7 MB
# Submission Id: 1052344457


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        len_r, len_c = len(mat), len(mat[0])
        
        def binary_search(row):
            left, right = 0, len_c
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 0:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        sum_mat = []
        for idx, row in enumerate(mat):
            sum_mat.append([idx, binary_search(row)])
            
        sum_mat.sort(key=lambda x: x[1])
        return [sum_mat[i][0] for i in range(k)]