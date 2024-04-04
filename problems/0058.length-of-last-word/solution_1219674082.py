# 0058 - Length of Last Word
# Date: 2024-04-01
# Runtime: 34 ms, Memory: 16.8 MB
# Submission Id: 1219674082


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        while n and s[n-1] == ' ':
            n -= 1
        
        ans = 0
        while n and s[n-1] != ' ':
            ans += 1
            n -= 1
        return ans