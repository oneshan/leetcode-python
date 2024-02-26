# 0191 - Number of 1 Bits
# Date: 2022-05-09
# Runtime: 67 ms, Memory: 13.8 MB
# Submission Id: 696166358


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            n &= n-1
            ans += 1
        return ans