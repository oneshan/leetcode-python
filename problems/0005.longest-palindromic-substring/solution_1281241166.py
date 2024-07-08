# 0005 - Longest Palindromic Substring
# Date: 2024-06-08
# Runtime: 85 ms, Memory: 16.6 MB
# Submission Id: 1281241166


class Solution:
    def longestPalindrome(self, s: str) -> str:
        trans_s = '#' + '#'.join(s) + '#'

        n = len(trans_s)
        p = [0] * n
        c = r = 0
        for i in range(1, n):
            if i > r:
                c = r = i
            else:
                p[i] = min(r-i, p[2*c-i])
            
            while (
                i-p[i]-1 >= 0
                and i+p[i]+1 < n
                and trans_s[i-p[i]-1] == trans_s[i+p[i]+1]
            ):
                p[i] += 1
            
            if i + p[i] > r:
                c, r = i, i+p[i]

        max_i = max_len = 0
        for i in range(n):
            if p[i] > max_len:
                max_i, max_len = i, p[i]

        start = (max_i - max_len) // 2
        return s[start:start+max_len]
        