# 3394 - Minimum Array End
# Date: 2024-04-28
# Runtime: 41 ms, Memory: 16.6 MB
# Submission Id: 1243765725


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bits = [0] * 64
        for i in range(64):
            bits[i] = bool((1 << i) & x)

        j = 0        
        for i in range(64):
            if j == 64:
                break
            while bits[j]:
                j += 1
            bits[j] |= bool((1 << i) & (n-1))
            j += 1

        ans = 0
        for i in range(63, -1, -1):
            ans = (ans << 1) | bits[i]

        return ans