# 1585 - The kth Factor of n
# Date: 2024-04-03
# Runtime: 40 ms, Memory: 16.6 MB
# Submission Id: 1222462967


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n+1):
            if n % i == 0:
                k -= 1
            if k == 0:
                return i
        return -1