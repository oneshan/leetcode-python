# 1732 - Minimum One Bit Operations to Make Integers Zero
# Date: 2023-11-30
# Runtime: 51 ms, Memory: 16.4 MB
# Submission Id: 1109419731


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        k = 1
        while (k << 1) <= n:
            k <<= 1
        
        return self.minimumOneBitOperations(k ^ (k >> 1) ^ n) + k