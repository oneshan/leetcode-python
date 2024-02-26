# 0005 - Longest Palindromic Substring
# Date: 2023-10-27
# Runtime: 423 ms, Memory: 16.2 MB
# Submission Id: 1085037008


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_len, ans_str = 0, ""

        def check_palindrome(left, right):
            nonlocal ans_len, ans_str
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > ans_len:
                    ans_len = right - left + 1
                    ans_str = s[left:right+1]
                left -= 1
                right += 1
        
        for i in range(n):
            check_palindrome(i, i)
            check_palindrome(i, i+1)
        return ans_str