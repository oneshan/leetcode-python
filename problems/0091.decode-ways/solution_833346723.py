# 0091 - Decode Ways
# Date: 2022-10-30
# Runtime: 52 ms, Memory: 13.8 MB
# Submission Id: 833346723


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        p2 = p1 = 1
        for i in range(1, len(s)):
            curr = 0
            if s[i] != '0':
                curr += p1
            if s[i-1] == '1' or (s[i-1] == '2' and int(s[i]) <= 6):
                curr += p2
            p2, p1 = p1, curr
        return p1
