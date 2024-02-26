# 0461 - Hamming Distance
# Date: 2022-12-06
# Runtime: 45 ms, Memory: 13.9 MB
# Submission Id: 855434550


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        ans = 0
        while num:
            num &= (num-1)
            ans += 1
        return ans