# 2487 - Optimal Partition of String
# Date: 2024-04-03
# Runtime: 86 ms, Memory: 17.5 MB
# Submission Id: 1222466905


class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        curr = set()
        for ch in s:
            if ch in curr:
                curr = set()
                ans += 1
            curr.add(ch)

        if curr:
            ans += 1
        return ans