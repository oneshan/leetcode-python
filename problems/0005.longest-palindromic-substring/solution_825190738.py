# 0005 - Longest Palindromic Substring
# Date: 2022-10-18
# Runtime: 2431 ms, Memory: 14 MB
# Submission Id: 825190738


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def calculate(left, right):
            count, pair = 0, (0, -1)
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
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
            if i < len(s)-1:
                count, pair = calculate(i, i+1)
                if count > max_len:
                    max_len, ans_idx = count, pair
        return s[ans_idx[0]: ans_idx[1]+1]