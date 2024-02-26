# 2575 - Minimum Cuts to Divide a Circle
# Date: 2022-11-26
# Runtime: 53 ms, Memory: 13.9 MB
# Submission Id: 850130650


class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        if n & 1:
            return n
        return n >> 1