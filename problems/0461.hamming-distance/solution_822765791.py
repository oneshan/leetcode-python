# 0461 - Hamming Distance
# Date: 2022-10-15
# Runtime: 45 ms, Memory: 13.7 MB
# Submission Id: 822765791


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        ans = 0
        while num:
            num &= num-1
            ans += 1
        return ans