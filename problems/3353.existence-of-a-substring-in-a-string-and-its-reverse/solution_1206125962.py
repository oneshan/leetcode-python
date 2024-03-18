# 3353 - Existence of a Substring in a String and Its Reverse
# Date: 2024-03-17
# Runtime: 39 ms, Memory: 16.5 MB
# Submission Id: 1206125962


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        n = len(s)

        for i in range(n-1):
            if s[i:i+2] in rev:
                return True
        return False