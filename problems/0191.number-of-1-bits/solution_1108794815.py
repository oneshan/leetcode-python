# 0191 - Number of 1 Bits
# Date: 2023-11-29
# Runtime: 41 ms, Memory: 16.4 MB
# Submission Id: 1108794815


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += 1
            n &= (n-1)
        return ans