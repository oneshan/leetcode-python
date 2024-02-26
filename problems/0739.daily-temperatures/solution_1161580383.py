# 0739 - Daily Temperatures
# Date: 2024-01-31
# Runtime: 886 ms, Memory: 29.9 MB
# Submission Id: 1161580383


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                ans[prev_idx] = idx - prev_idx
            stack.append(idx)
        return ans