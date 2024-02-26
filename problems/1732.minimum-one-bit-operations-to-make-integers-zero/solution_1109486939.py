# 1732 - Minimum One Bit Operations to Make Integers Zero
# Date: 2023-11-30
# Runtime: 33 ms, Memory: 16.2 MB
# Submission Id: 1109486939


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        while n:
            ans = -ans - (n ^ (n-1))
            n &= n - 1
        return abs(ans)