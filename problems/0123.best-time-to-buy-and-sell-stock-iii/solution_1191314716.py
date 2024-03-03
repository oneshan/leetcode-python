# 0123 - Best Time to Buy and Sell Stock III
# Date: 2024-03-02
# Runtime: 784 ms, Memory: 30.4 MB
# Submission Id: 1191314716


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        t1 = [float('inf'), 0]
        t2 = [float('inf'), 0]

        for price in prices:

            t1[0] = min(t1[0], price)
            t1[1] = max(t1[1], price - t1[0])

            t2[0] = min(t2[0], price - t1[1])
            t2[1] = max(t2[1], price - t2[0])

        return t2[1]    