# 0191 - Number of 1 Bits
# Date: 2024-02-06
# Runtime: 39 ms, Memory: 16.5 MB
# Submission Id: 1167687957


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n-1)
            ans += 1
        return ans