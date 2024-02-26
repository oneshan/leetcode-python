# 0739 - Daily Temperatures
# Date: 2022-09-30
# Runtime: 1941 ms, Memory: 25.1 MB
# Submission Id: 812039556


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