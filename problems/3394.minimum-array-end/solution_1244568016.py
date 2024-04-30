# 3394 - Minimum Array End
# Date: 2024-04-29
# Runtime: 35 ms, Memory: 16.5 MB
# Submission Id: 1244568016


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        n -= 1
        for i in range(64):
            if (1 << i) & ans:
                continue
            if n == 0:
                break
            ans |= (n & 1) << i
            n >>= 1
        return ans