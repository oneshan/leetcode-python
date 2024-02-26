# 0014 - Longest Common Prefix
# Date: 2024-02-16
# Runtime: 37 ms, Memory: 16.5 MB
# Submission Id: 1176656349


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        m = min(len(s) for s in strs)
        for j in range(m):
            for i in range(n):
                if strs[i][j] != strs[0][j]:
                    return strs[0][:j]
        return strs[0][:m]