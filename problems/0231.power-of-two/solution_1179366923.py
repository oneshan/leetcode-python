# 0231 - Power of Two
# Date: 2024-02-19
# Runtime: 28 ms, Memory: 16.5 MB
# Submission Id: 1179366923


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return n & (n-1) == 0