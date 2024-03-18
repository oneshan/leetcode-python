# 1909 - Buildings With an Ocean View
# Date: 2024-03-17
# Runtime: 529 ms, Memory: 34 MB
# Submission Id: 1206282596


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack