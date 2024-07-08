# 0084 - Largest Rectangle in Histogram
# Date: 2024-05-12
# Runtime: 663 ms, Memory: 30.5 MB
# Submission Id: 1256011202


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []  # mono increasing (height, idx)

        ans = 0
        for idx, height in enumerate(heights):
            prev_i = idx
            while stack and stack[-1][0] >= height:
                prev_h, prev_i = stack.pop()
                ans = max(ans, (idx - prev_i) * prev_h)
            stack.append((height, prev_i))

        while stack:
            prev_h, prev_i = stack.pop()
            ans = max(ans, (n-prev_i) * prev_h)

        return ans