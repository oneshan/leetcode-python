# 0014 - Longest Common Prefix
# Date: 2022-05-03
# Runtime: 36 ms, Memory: 14 MB
# Submission Id: 692377136


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        ans = len(strs[0])
        for string in strs:
            ans = min(ans, len(string))
            for ptr in range(ans):
                if string[ptr] != strs[0][ptr]:
                    ans = ptr
                    break
        return strs[0][:ans]