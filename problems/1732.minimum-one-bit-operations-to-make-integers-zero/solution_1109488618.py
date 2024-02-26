# 1732 - Minimum One Bit Operations to Make Integers Zero
# Date: 2023-11-30
# Runtime: 37 ms, Memory: 16.2 MB
# Submission Id: 1109488618


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = n
        while n:
            n >>= 1
            ans ^= n
        return ans