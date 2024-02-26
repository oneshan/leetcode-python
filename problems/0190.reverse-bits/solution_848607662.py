# 0190 - Reverse Bits
# Date: 2022-11-23
# Runtime: 24 ms, Memory: 13.9 MB
# Submission Id: 848607662


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans