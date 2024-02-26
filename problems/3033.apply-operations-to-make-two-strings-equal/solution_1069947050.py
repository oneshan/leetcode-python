# 3033 - Apply Operations to Make Two Strings Equal
# Date: 2023-10-08
# Runtime: 40 ms, Memory: 16.4 MB
# Submission Id: 1069947050


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        
        p1, p0 = 0, -1
        left, diffs = inf, 0
        for right in range(n):
            if s1[right] == s2[right]:
                continue
            if left == inf:
                p0 = x/2
            else:
                p1, p0 = p0, min(p0 + x/2, p1 + right - left)
            left = right
            diffs += 1

        if diffs & 1:
            return -1
        if diffs == 0:
            return 0
        return int(p0)