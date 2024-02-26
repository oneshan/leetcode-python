# 2487 - Optimal Partition of String
# Date: 2023-04-04
# Runtime: 122 ms, Memory: 14.6 MB
# Submission Id: 927626396


class Solution:
    def partitionString(self, s: str) -> int:
        loc = {}
        ans, left = 1, 0
        for idx, ch in enumerate(s):
            if loc.get(ch, -1) >= left:
                left = idx
                ans += 1
            loc[ch] = idx
        return ans