# 2325 - Number of Ways to Select Buildings
# Date: 2024-07-17
# Runtime: 234 ms, Memory: 17.5 MB
# Submission Id: 1323561901


class Solution:
    def numberOfWays(self, s: str) -> int:
        ans = c0 = c1 = c01 = c10 = 0
        for ch in s:
            if ch == '1':
                ans += c10  # 101
                c01 += c0
                c1 += 1
            else:
                ans += c01  # 010
                c10 += c1
                c0 += 1
        return ans