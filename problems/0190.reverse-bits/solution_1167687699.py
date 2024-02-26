# 0190 - Reverse Bits
# Date: 2024-02-06
# Runtime: 45 ms, Memory: 16.6 MB
# Submission Id: 1167687699


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans