# 3033 - Apply Operations to Make Two Strings Equal
# Date: 2023-10-08
# Runtime: 42 ms, Memory: 16.2 MB
# Submission Id: 1069948574


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        
        dp1 = dp0 = 0
        left, diffs = inf, 0
        for right in range(n):
            if s1[right] == s2[right]:
                continue
            if left == inf:
                dp0 = x/2
            else:
                dp1, dp0 = dp0, min(dp0 + x/2, dp1 + right - left)
            left = right
            diffs += 1

        if diffs & 1:
            return -1
        if diffs == 0:
            return 0
        return int(dp0)