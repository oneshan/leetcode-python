# 0005 - Longest Palindromic Substring
# Date: 2024-02-23
# Runtime: 612 ms, Memory: 16.6 MB
# Submission Id: 1183621686


class Solution:
    def longestPalindrome(self, s: str) -> str:
        trans_s = '#'.join(f'^{s}$')
        n = len(trans_s)

        p = [0] * n
        c = r = 0
        for i in range(1, n-1):
            p[i] = (r > i) and min(r-i, p[2*c-i])
            while trans_s[i+1+p[i]] == trans_s[i-1-p[i]]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, p[i]
        
        max_len, center_idx = max((val, idx) for idx, val in enumerate(p))
        start_idx = (center_idx - max_len) // 2
        return s[start_idx: start_idx+max_len]