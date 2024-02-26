# 0121 - Best Time to Buy and Sell Stock
# Date: 2023-07-24
# Runtime: 1083 ms, Memory: 27.4 MB
# Submission Id: 1002613453


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, curr_min = 0, float('inf')
        for num in prices:
            curr_min = min(curr_min, num)
            ans = max(ans, num - curr_min)
        return ans