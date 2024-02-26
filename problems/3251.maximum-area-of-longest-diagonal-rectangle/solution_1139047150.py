# 3251 - Maximum Area of Longest Diagonal Rectangle
# Date: 2024-01-07
# Runtime: 62 ms, Memory: 17.2 MB
# Submission Id: 1139047150


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area, max_diag = -1, -1
        for length, width in dimensions:
            diag = length ** 2 + width ** 2
            if diag > max_diag:
                max_diag = diag
                max_area = length * width
            elif diag == max_diag:
                max_area = max(max_area, length * width)
        return max_area