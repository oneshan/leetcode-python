# 3033 - Apply Operations to Make Two Strings Equal
# Date: 2023-10-08
# Runtime: 39 ms, Memory: 17.1 MB
# Submission Id: 1069931058


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diffs = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(diffs) & 1:
            return -1
        
        @cache
        def dp(i):
            if i == 0:
                return x / 2
            if i == -1:
                return 0
            return min(
                dp(i - 1) + x / 2,
                dp(i - 2) + diffs[i] - diffs[i-1]
            )
        
        return int(dp(len(diffs) - 1))