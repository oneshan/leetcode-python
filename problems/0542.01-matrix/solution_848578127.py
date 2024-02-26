# 0542 - 01 Matrix
# Date: 2022-11-23
# Runtime: 1816 ms, Memory: 17 MB
# Submission Id: 848578127


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(mat), len(mat[0])
        
        ans = [[float('inf')] * len_c for _ in range(len_r)]
        
        for r in range(len_r):
            for c in range(len_c):
                if mat[r][c] == 0:
                    ans[r][c] = 0
                else:
                    if r:
                        ans[r][c] = min(ans[r][c], ans[r-1][c] + 1)
                    if c:
                        ans[r][c] = min(ans[r][c], ans[r][c-1] + 1)
        
        for r in range(len_r-1, -1, -1):
            for c in range(len_c-1, -1, -1):
                if r < len_r - 1:
                    ans[r][c] = min(ans[r][c], ans[r+1][c] + 1)
                if c < len_c - 1:
                    ans[r][c] = min(ans[r][c], ans[r][c+1] + 1)
        
        return ans