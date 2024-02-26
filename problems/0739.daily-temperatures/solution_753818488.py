# 0739 - Daily Temperatures
# Date: 2022-07-22
# Runtime: 1893 ms, Memory: 25.1 MB
# Submission Id: 753818488


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        hottest = 0
        
        for idx in range(n-1, -1, -1):
            if temperatures[idx] >= hottest:
                hottest = temperatures[idx]
                continue
            days = 1
            while temperatures[idx + days] <= temperatures[idx]:
                days += ans[idx+days]
            ans[idx] = days

        return ans