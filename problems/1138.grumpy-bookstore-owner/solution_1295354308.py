# 1138 - Grumpy Bookstore Owner
# Date: 2024-06-21
# Runtime: 209 ms, Memory: 18.8 MB
# Submission Id: 1295354308


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        satified = sum(c for c, g in zip(customers, grumpy) if g == 0)
        ans = 0

        for i in range(n):
            if i >= minutes and grumpy[i-minutes]:
                satified -= customers[i-minutes]
            if grumpy[i]:
                satified += customers[i]
            ans = max(ans, satified)
        return ans