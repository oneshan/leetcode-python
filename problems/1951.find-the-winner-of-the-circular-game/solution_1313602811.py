# 1951 - Find the Winner of the Circular Game
# Date: 2024-07-08
# Runtime: 26 ms, Memory: 16.4 MB
# Submission Id: 1313602811


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n+1):
            ans = (ans + k) % i
        return ans + 1