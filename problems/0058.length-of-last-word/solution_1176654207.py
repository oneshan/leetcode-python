# 0058 - Length of Last Word
# Date: 2024-02-16
# Runtime: 33 ms, Memory: 16.5 MB
# Submission Id: 1176654207


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