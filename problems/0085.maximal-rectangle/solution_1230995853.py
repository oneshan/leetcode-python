# 0085 - Maximal Rectangle
# Date: 2024-04-13
# Runtime: 214 ms, Memory: 17.9 MB
# Submission Id: 1230995853


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])

        def get_area(heights):
            res = 0
            stack = [-1]
            for i in range(len_c+1):
                while stack[-1] != -1 and (i == len_c or heights[stack[-1]] >= heights[i]):
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    res = max(res, height * width)
                stack.append(i)
            return res

        ans = 0
        dp = [0] * len_c
        for r in range(len_r):
            for c in range(len_c):
                dp[c] = dp[c] + 1 if matrix[r][c] == '1' else 0
            ans = max(ans, get_area(dp))
        return ans