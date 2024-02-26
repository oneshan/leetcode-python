# 0190 - Reverse Bits
# Date: 2024-02-07
# Runtime: 38 ms, Memory: 16.5 MB
# Submission Id: 1168564887


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans