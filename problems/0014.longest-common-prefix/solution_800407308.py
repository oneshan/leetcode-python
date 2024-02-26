# 0014 - Longest Common Prefix
# Date: 2022-09-15
# Runtime: 51 ms, Memory: 13.9 MB
# Submission Id: 800407308


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        
        max_len = len(strs[0])
        for idx in range(max_len):
            for s in strs:
                if idx == len(s) or s[idx] != strs[0][idx]:
                    return strs[0][:idx]
        return strs[0]
