# 1817 - Calculate Money in Leetcode Bank
# Date: 2023-12-06
# Runtime: 42 ms, Memory: 16.2 MB
# Submission Id: 1113639157


class Solution:
    def totalMoney(self, n: int) -> int:
        week, day = divmod(n, 7)
        
        first, last = 28, 28 + (week-1) * 7
        ans = (first + last) * week // 2
        
        ans += (1 + week) * day
        for i in range(day):
            ans += i
        return ans