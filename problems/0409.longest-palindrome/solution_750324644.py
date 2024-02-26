# 0409 - Longest Palindrome
# Date: 2022-07-18
# Runtime: 50 ms, Memory: 13.9 MB
# Submission Id: 750324644


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans, table = 0, {}
        for ch in s:
            table[ch] = table.get(ch, 0) ^ 1
            if table[ch] == 0:
                ans += 2
        
        if ans < len(s):
            ans += 1
        return ans