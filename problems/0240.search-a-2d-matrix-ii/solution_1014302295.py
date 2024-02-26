# 0240 - Search a 2D Matrix II
# Date: 2023-08-07
# Runtime: 167 ms, Memory: 22.8 MB
# Submission Id: 1014302295


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_r, len_c = len(matrix), len(matrix[0])
        
        r, c = len_r -1, 0
        while r >= 0 and c < len_c:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False