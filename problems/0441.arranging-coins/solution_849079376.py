# 0441 - Arranging Coins
# Date: 2022-11-24
# Runtime: 75 ms, Memory: 13.8 MB
# Submission Id: 849079376


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            layer = (left + right) // 2
            value = (1+layer) * layer // 2
            if value == n:
                return layer
            if value < n:
                left = layer + 1
            else:
                right = layer - 1
        return right