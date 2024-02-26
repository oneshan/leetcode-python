# 0739 - Daily Temperatures
# Date: 2022-07-22
# Runtime: 1888 ms, Memory: 25.1 MB
# Submission Id: 753745812


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_idx = stack.pop()[1]
                ans[prev_idx] = idx - prev_idx
            stack.append((temp, idx))
        return ans