# 1146 - Greatest Common Divisor of Strings
# Date: 2023-02-01
# Runtime: 31 ms, Memory: 13.8 MB
# Submission Id: 889227153


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        def is_concat(s, length):
            for idx, ch in enumerate(s):
                if ch != str1[idx % length]:
                    return False
            return True
        
        max_length = gcd(len(str1), len(str2))
        if is_concat(str1, max_length) and is_concat(str2, max_length):
            return str1[:max_length]
        return ''