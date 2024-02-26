# 0120 - Triangle
# Date: 2024-02-23
# Runtime: 61 ms, Memory: 17.6 MB
# Submission Id: 1183593822


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        prev = triangle[-1]
        for i in range(n-2, -1, -1):
            curr = [0] * n
            for j in range(i+1):
                curr[j] = triangle[i][j] + min(prev[j], prev[j+1])
            prev = curr
        return prev[0]