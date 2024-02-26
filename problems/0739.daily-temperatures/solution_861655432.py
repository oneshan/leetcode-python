# 0739 - Daily Temperatures
# Date: 2022-12-18
# Runtime: 3087 ms, Memory: 28.5 MB
# Submission Id: 861655432


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append(i)
        return ans