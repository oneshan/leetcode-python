# 2487 - Optimal Partition of String
# Date: 2024-04-03
# Runtime: 105 ms, Memory: 17.5 MB
# Submission Id: 1222467572


class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        curr = 0
        for ch in s:
            mask = 1 << (ord(ch) - ord('a'))
            if curr & mask:
                curr = 0
                ans += 1
            curr |= mask

        if curr:
            ans += 1
        return ans