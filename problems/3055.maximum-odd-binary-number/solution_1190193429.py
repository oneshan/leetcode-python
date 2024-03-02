# 3055 - Maximum Odd Binary Number
# Date: 2024-03-01
# Runtime: 35 ms, Memory: 16.4 MB
# Submission Id: 1190193429


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        count = sum(ch == '1' for ch in s) - 1
        
        ans = []
        for i in range(n-1):
            ans.append('1' if count > i else '0')
        ans.append('1')
        return ''.join(ans)