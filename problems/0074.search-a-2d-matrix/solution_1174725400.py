# 0074 - Search a 2D Matrix
# Date: 2024-02-14
# Runtime: 46 ms, Memory: 17 MB
# Submission Id: 1174725400


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_r, len_c = len(matrix), len(matrix[0])

        left, right = 0, len_r * len_c - 1
        while left <= right:
            mid = (left + right) // 2
            r, c = divmod(mid, len_c)
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False