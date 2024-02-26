# 0191 - Number of 1 Bits
# Date: 2022-11-01
# Runtime: 65 ms, Memory: 13.8 MB
# Submission Id: 834673676


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= n-1
            ans += 1
        return ans