# 1666 - Make The String Great
# Date: 2022-09-29
# Runtime: 91 ms, Memory: 13.8 MB
# Submission Id: 811417544


class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        
        end = 0
        for idx in range(len(s)):
            if end and abs(ord(s[idx]) - ord(s[end-1])) == 32:
                end -= 1
            else:
                s[end] = s[idx]
                end += 1
        return ''.join(s[:end])