# 1961 - Maximum Ice Cream Bars
# Date: 2022-10-10
# Runtime: 1084 ms, Memory: 28 MB
# Submission Id: 819300817


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