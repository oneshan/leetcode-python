# 1146 - Greatest Common Divisor of Strings
# Date: 2023-02-01
# Runtime: 38 ms, Memory: 13.9 MB
# Submission Id: 889223970


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]