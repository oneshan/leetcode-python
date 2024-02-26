# 0981 - Delete Columns to Make Sorted
# Date: 2023-01-03
# Runtime: 235 ms, Memory: 14.6 MB
# Submission Id: 870514258


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        ans = 0
        for i in range(m):
            for j in range(1, n):
                if ord(strs[j][i]) < ord(strs[j-1][i]):
                    ans += 1
                    break
        return ans