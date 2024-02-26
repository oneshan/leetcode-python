# 0005 - Longest Palindromic Substring
# Date: 2023-10-27
# Runtime: 547 ms, Memory: 16.4 MB
# Submission Id: 1085036315


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def calculate(left, right):
            count, pair = 0, (0, -1)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count = right - left + 1
                pair = (left, right)
                left -= 1
                right += 1
            return count, pair
        
        max_len, ans_idx = 1, (0, 0)
        for i in range(len(s)):
            count, pair = calculate(i, i)
            if count > max_len:
                max_len, ans_idx = count, pair
            count, pair = calculate(i, i+1)
            if count > max_len:
                max_len, ans_idx = count, pair
        return s[ans_idx[0]: ans_idx[1]+1]