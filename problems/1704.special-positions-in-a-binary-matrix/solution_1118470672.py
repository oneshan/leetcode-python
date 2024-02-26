# 1704 - Special Positions in a Binary Matrix
# Date: 2023-12-13
# Runtime: 169 ms, Memory: 16.7 MB
# Submission Id: 1118470672


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        len_r, len_c = len(mat), len(mat[0])
        rows = [0] * len_r
        cols = [0] * len_c
        
        for r in range(len_r):
            for c in range(len_c):
                rows[r] += mat[r][c]
                cols[c] += mat[r][c]
        ans = 0
        for r in range(len_r):
            for c in range(len_c):
                if mat[r][c] and rows[r] == cols[c] == 1:
                    ans += 1
        return ans