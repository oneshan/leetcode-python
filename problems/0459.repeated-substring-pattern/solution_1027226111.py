# 0459 - Repeated Substring Pattern
# Date: 2023-08-21
# Runtime: 43 ms, Memory: 16.4 MB
# Submission Id: 1027226111


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        return s in t[1:-1]