# 1138 - Grumpy Bookstore Owner
# Date: 2024-06-21
# Runtime: 218 ms, Memory: 18.7 MB
# Submission Id: 1295352280


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        total = sum(c for c, g in zip(customers, grumpy) if g == 0)

        left = curr = 0
        max_g = 0
        for right in range(n):
            if grumpy[right] == 1:
                curr += customers[right]
            if right >= minutes:
                if grumpy[left] == 1:
                    curr -= customers[left]
                left += 1
            max_g = max(max_g, curr)

        return total + max_g