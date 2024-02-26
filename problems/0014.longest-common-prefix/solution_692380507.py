# 0014 - Longest Common Prefix
# Date: 2022-05-03
# Runtime: 65 ms, Memory: 14 MB
# Submission Id: 692380507


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        ptr = 0
        while ptr < len(strs[0]):
            for string in strs:
                if len(string) - 1 < ptr:
                    return strs[0][:ptr]
                if string[ptr] != strs[0][ptr]:
                    return strs[0][:ptr]
            ptr += 1
        return strs[0][:ptr]