# 0014 - Longest Common Prefix
# Date: 2024-05-05
# Runtime: 42 ms, Memory: 16.7 MB
# Submission Id: 1249858859


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]