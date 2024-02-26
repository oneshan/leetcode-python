# 0392 - Is Subsequence
# Date: 2022-07-11
# Runtime: 40 ms, Memory: 13.8 MB
# Submission Id: 744097010


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        ps = pt = 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
            else:
                pt += 1
        return ps == len(s)