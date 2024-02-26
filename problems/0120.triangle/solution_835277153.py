# 0120 - Triangle
# Date: 2022-11-02
# Runtime: 156 ms, Memory: 14.9 MB
# Submission Id: 835277153


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for row in range(1, n):
            for col in range(row+1):
                min_val = float('inf')
                if col > 0:
                    min_val = triangle[row-1][col-1]
                if col < row:
                    min_val = min(min_val, triangle[row-1][col])
                triangle[row][col] += min_val
        return min(triangle[-1])