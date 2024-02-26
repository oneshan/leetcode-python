# 0459 - Repeated Substring Pattern
# Date: 2023-08-21
# Runtime: 1528 ms, Memory: 16.3 MB
# Submission Id: 1027220286


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for chunk_size in range(1, n // 2 + 1):
            if n % chunk_size != 0:
                continue
            can_split = True
            for i in range(chunk_size, n):
                if s[i-chunk_size] != s[i]:
                    can_split = False
            if can_split:
                return True
        return False