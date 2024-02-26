# 0014 - Longest Common Prefix
# Date: 2022-09-15
# Runtime: 72 ms, Memory: 13.9 MB
# Submission Id: 800406419


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        
        for j in range(len(strs[0])):
            ch = strs[0][j]
            for i in range(len(strs)):
                if j == len(strs[i]) or strs[i][j] != ch:
                    return strs[0][:j]
        return strs[0]
