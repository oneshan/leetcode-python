# 1961 - Maximum Ice Cream Bars
# Date: 2023-01-06
# Runtime: 1966 ms, Memory: 28 MB
# Submission Id: 872563545


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for cost in costs:
            if cost > coins:
                break
            ans += 1
            coins -= cost
        return ans