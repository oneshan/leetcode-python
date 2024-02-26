# 0459 - Repeated Substring Pattern
# Date: 2023-08-21
# Runtime: 202 ms, Memory: 16.5 MB
# Submission Id: 1027224640


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for chunk_size in range(1, n // 2 + 1):
            if n % chunk_size != 0:
                continue
            for i in range(chunk_size, n):
                if s[i-chunk_size] != s[i]:
                    break
            else:
                return True
        return False