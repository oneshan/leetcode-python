# 1441 - Minimum Flips to Make a OR b Equal to c
# Date: 2023-06-08
# Runtime: 37 ms, Memory: 16.4 MB
# Submission Id: 966220425


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            if c & 1:
                ans += 0 if (a & 1) or (b & 1) else 1
            else:
                ans += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1
        return ans