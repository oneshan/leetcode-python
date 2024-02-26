# 0191 - Number of 1 Bits
# Date: 2022-11-10
# Runtime: 72 ms, Memory: 13.9 MB
# Submission Id: 840747468


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= n-1
            ans += 1
        return ans