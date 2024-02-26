# 1806 - Count of Matches in Tournament
# Date: 2023-12-05
# Runtime: 37 ms, Memory: 16.3 MB
# Submission Id: 1112774912


class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n != 1:
            ans += (n >> 1)
            if n & 1:
                n = (n >> 1) + 1
            else:
                n >>= 1
        return ans