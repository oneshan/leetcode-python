# 0461 - Hamming Distance
# Date: 2022-12-06
# Runtime: 56 ms, Memory: 13.9 MB
# Submission Id: 855434079


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            ans += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        return ans