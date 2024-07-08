# 0409 - Longest Palindrome
# Date: 2024-06-04
# Runtime: 41 ms, Memory: 16.5 MB
# Submission Id: 1276953713


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        has_odd = False
        ans = 0
        for count in counter.values():
            ans += count - (count & 1)
            if count & 1:
                has_odd = True
        
        return ans + int(has_odd)