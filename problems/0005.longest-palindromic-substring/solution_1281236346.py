# 0005 - Longest Palindromic Substring
# Date: 2024-06-08
# Runtime: 305 ms, Memory: 16.5 MB
# Submission Id: 1281236346


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        self.max_len, self.max_left = 1, 0

        def check_palindrome(left, right):
            while left >= 0 and right < n:
                if s[left] != s[right]:
                    return
                if (right-left+1) > self.max_len:
                    self.max_len, self.max_left = (right-left+1), left
                left -= 1
                right += 1

        for i in range(1, n):
            check_palindrome(i, i)
            check_palindrome(i, i-1)

        return s[self.max_left:self.max_left+self.max_len]