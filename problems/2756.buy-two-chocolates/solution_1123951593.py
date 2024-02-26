# 2756 - Buy Two Chocolates
# Date: 2023-12-20
# Runtime: 72 ms, Memory: 16.2 MB
# Submission Id: 1123951593


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        total = prices[0] + prices[1]
        return money - total if total <= money else money