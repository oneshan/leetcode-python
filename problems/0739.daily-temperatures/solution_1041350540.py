# 0739 - Daily Temperatures
# Date: 2023-09-05
# Runtime: 1035 ms, Memory: 30.3 MB
# Submission Id: 1041350540


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