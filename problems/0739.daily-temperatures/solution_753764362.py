# 0739 - Daily Temperatures
# Date: 2022-07-22
# Runtime: 2053 ms, Memory: 24.8 MB
# Submission Id: 753764362


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                ans[prev_idx] = idx - prev_idx
            stack.append(idx)
        return ans