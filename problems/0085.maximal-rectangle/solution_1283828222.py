# 0085 - Maximal Rectangle
# Date: 2024-06-10
# Runtime: 210 ms, Memory: 17.9 MB
# Submission Id: 1283828222


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])

        def get_area(heights):
            res = 0
            stack = []
            for idx, height in enumerate(heights):
                prev_i = idx
                while stack and stack[-1][0] >= height:
                    prev_h, prev_i = stack.pop()
                    res = max(res, (idx - prev_i) * prev_h)
                stack.append((height, prev_i))

            while stack:
                prev_h, prev_i = stack.pop()
                res = max(res, (len_c-prev_i) * prev_h)

            return res

        ans = 0
        dp = [0] * len_c
        for r in range(len_r):
            for c in range(len_c):
                dp[c] = dp[c] + 1 if matrix[r][c] == '1' else 0
            ans = max(ans, get_area(dp))
        return ans