# 0461 - Hamming Distance
# Date: 2023-09-24
# Runtime: 40 ms, Memory: 16.2 MB
# Submission Id: 1057862156


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        ans = 0
        while num:
            num &= num-1
            ans += 1
        return ans