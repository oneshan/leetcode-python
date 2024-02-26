# 3033 - Apply Operations to Make Two Strings Equal
# Date: 2023-10-08
# Runtime: 154 ms, Memory: 29.2 MB
# Submission Id: 1069934669


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        
        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(diff) & 1:
            return -1
        
        @cache
        def helper(left, right):
            if left > right:
                return 0
            return min(
                helper(left+2, right) + diff[left+1] - diff[left],
                helper(left, right-2) + diff[right] - diff[right-1],
                helper(left+1, right-1) + x,
            )
            return ret
        
        return helper(0, len(diff)-1)
        
        