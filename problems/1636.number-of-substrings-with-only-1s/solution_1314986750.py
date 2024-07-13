# 1636 - Number of Substrings With Only 1s
# Date: 2024-07-09
# Runtime: 59 ms, Memory: 17.2 MB
# Submission Id: 1314986750


class Solution:
    def numSub(self, s: str) -> int:
        MOD = 1_000_000_007
        ans = 0
        left = -1
        for right in range(len(s)):
            if s[right] == '0':
                left = right
            ans += (right - left)

        return ans % MOD