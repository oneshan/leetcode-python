# 0650 - 2 Keys Keyboard
# Date: 2024-06-11
# Runtime: 30 ms, Memory: 16.5 MB
# Submission Id: 1284686803


class Solution:
    def minSteps(self, n: int) -> int:
        i, ans = 2, 0
        while n > 1:
            while n % i == 0:
                n //= i
                ans += i
            i += 1

        return ans