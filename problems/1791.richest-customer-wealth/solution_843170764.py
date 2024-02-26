# 1791 - Richest Customer Wealth
# Date: 2022-11-14
# Runtime: 62 ms, Memory: 13.8 MB
# Submission Id: 843170764


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for account in accounts:
            ans = max(ans, sum(account))
        return ans