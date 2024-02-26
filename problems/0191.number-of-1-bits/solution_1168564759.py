# 0191 - Number of 1 Bits
# Date: 2024-02-07
# Runtime: 32 ms, Memory: 16.5 MB
# Submission Id: 1168564759


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n-1)
            ans += 1
        return ans