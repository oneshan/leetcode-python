# 0120 - Triangle
# Date: 2024-02-23
# Runtime: 68 ms, Memory: 17.6 MB
# Submission Id: 1183595027


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        ans = triangle[-1][:]
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                ans[j] = triangle[i][j] + min(ans[j], ans[j+1])
        return ans[0]