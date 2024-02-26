# 3033 - Apply Operations to Make Two Strings Equal
# Date: 2023-10-08
# Runtime: 48 ms, Memory: 16.1 MB
# Submission Id: 1069962685


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        dp1, dp0 = inf, 0
        cost, diffs = 1, 0
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                cost += 1
            else:
                dp1, dp0 = dp0, min(dp0 + x/2, dp1 + cost)
                cost = 1
                diffs += 1

        if diffs & 1:
            return -1
        return int(dp0)