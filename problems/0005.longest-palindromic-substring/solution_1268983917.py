# 0005 - Longest Palindromic Substring
# Date: 2024-05-27
# Runtime: 76 ms, Memory: 16.4 MB
# Submission Id: 1268983917


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

            j = p[i] + 1
            while i - j >= 0 and i + j < n and trans_s[i-j] == trans_s[i+j]:
                j += 1
            p[i] = j - 1

            if i + p[i] > r:
                c, r = i, i + p[i]

        max_len, idx = max((val, idx) for idx, val in enumerate(p))
        start_idx = (idx - max_len) // 2
        return s[start_idx:start_idx+max_len]