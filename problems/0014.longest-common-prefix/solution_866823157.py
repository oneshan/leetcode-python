# 0014 - Longest Common Prefix
# Date: 2022-12-28
# Runtime: 34 ms, Memory: 13.8 MB
# Submission Id: 866823157


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not len(strs[0]):
            return ''
        
        n = len(strs)
        m = len(strs[0])
        
        for i in range(m):
            for s in strs:
                if len(s) == i:
                    return s[:i]
                if s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]