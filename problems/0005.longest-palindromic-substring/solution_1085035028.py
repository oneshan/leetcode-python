# 0005 - Longest Palindromic Substring
# Date: 2023-10-27
# Runtime: 403 ms, Memory: 16.3 MB
# Submission Id: 1085035028


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        ans = [0, 0]
        for i in range(n):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]
            
            even_length = expand(i, i+1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        return s[ans[0]: ans[1]+1]