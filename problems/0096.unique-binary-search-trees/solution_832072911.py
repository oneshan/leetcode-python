# 0096 - Unique Binary Search Trees
# Date: 2022-10-28
# Runtime: 57 ms, Memory: 13.9 MB
# Submission Id: 832072911


class Solution:
    def numTrees(self, n: int) -> int:
        ans = 1
        for i in range(n):
            ans = ans * 2 * (2*i+1) / (i+2) 
        return int(ans)