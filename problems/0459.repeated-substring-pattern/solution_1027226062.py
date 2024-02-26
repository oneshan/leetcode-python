# 0459 - Repeated Substring Pattern
# Date: 2023-08-21
# Runtime: 37 ms, Memory: 16.5 MB
# Submission Id: 1027226062


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        t = s + s
        return s in t[1:-1]