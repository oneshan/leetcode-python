# 0566 - Reshape the Matrix
# Date: 2022-11-15
# Runtime: 205 ms, Memory: 14.8 MB
# Submission Id: 843637390


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m*n != r*c:
            return mat
        
        ans = [ [0] * c for _ in range(r)]
        for i in range(m*n):
            old_r, old_c = divmod(i, n)
            new_r, new_c = divmod(i, c)
            ans[new_r][new_c] = mat[old_r][old_c]
        return ans