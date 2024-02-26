# 0191 - Number of 1 Bits
# Date: 2022-05-23
# Runtime: 39 ms, Memory: 13.9 MB
# Submission Id: 705157620


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            n &= n-1
            ans += 1
        return ans