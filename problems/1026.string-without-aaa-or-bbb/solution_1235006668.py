# 1026 - String Without AAA or BBB
# Date: 2024-04-17
# Runtime: 42 ms, Memory: 16.7 MB
# Submission Id: 1235006668


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        ca = cb = 0
        for _ in range(a+b):
            if (a > b and ca < 2) or cb == 2:
                ans.append('a')
                a -= 1
                ca, cb = ca+1, 0
            else:
                ans.append('b')
                b -= 1
                ca, cb = 0, cb+1
        return ''.join(ans)