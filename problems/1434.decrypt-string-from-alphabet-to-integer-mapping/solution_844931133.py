# 1434 - Decrypt String from Alphabet to Integer Mapping
# Date: 2022-11-17
# Runtime: 62 ms, Memory: 13.8 MB
# Submission Id: 844931133


class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        
        i = len(s)-1
        while i >= 0:
            if s[i] == '#':
                digits = int(s[i-2:i])
                i -= 3
            else:
                digits = int(s[i])
                i -= 1
            ans.append(chr(ord('a') + digits - 1))
        return ''.join(ans[::-1])