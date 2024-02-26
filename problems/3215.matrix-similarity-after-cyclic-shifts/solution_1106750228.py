# 3215 - Matrix Similarity After Cyclic Shifts
# Date: 2023-11-26
# Runtime: 113 ms, Memory: 16.3 MB
# Submission Id: 1106750228


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        len_r, len_c = len(mat), len(mat[0])
        
        for r in range(len_r):
            for c in range(len_c):
                if mat[r][c] != mat[r][(c+k) % len_c]:
                    return False
        return True