# 0014 - Longest Common Prefix
# Date: 2022-07-14
# Runtime: 84 ms, Memory: 14 MB
# Submission Id: 746509703


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = len(strs[0])
        for i in range(1, len(strs)):
            ans = min(ans, len(strs[i]))
            for j in range(ans):
                if strs[0][j] != strs[i][j]:
                    ans = j
                    break
        return strs[0][:ans]