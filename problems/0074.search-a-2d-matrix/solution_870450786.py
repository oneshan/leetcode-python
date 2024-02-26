# 0074 - Search a 2D Matrix
# Date: 2023-01-03
# Runtime: 118 ms, Memory: 14.5 MB
# Submission Id: 870450786


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_r, len_c = len(matrix), len(matrix[0])
        left, right = 0, len_r * len_c - 1
        while left <= right:
            mid = (left + right) // 2
            r, c = divmod(mid, len_c)
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False