# 1817 - Calculate Money in Leetcode Bank
# Date: 2023-12-06
# Runtime: 48 ms, Memory: 16.1 MB
# Submission Id: 1113637312


class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        week = 0
        for i in range(n):
            if i > 6 and i % 7 == 0:
                week += 1
            ans += (i % 7) + 1 + week
        return ans