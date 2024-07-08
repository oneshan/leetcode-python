# 0647 - Palindromic Substrings
# Date: 2024-05-27
# Runtime: 472 ms, Memory: 16.5 MB
# Submission Id: 1269003799


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        trans = '#'.join(f'^{s}$')
        trans = '#' + '#'.join(s) + '#'
        n = len(trans)

        p = [0] * n
        c = r = 0

        for i in range(1, n-1):
            if r > i:
                p[i] = min(r-i, p[2*c-i])
            else:
                c = r = i

            while (
                i + 1 + p[i] < n
                and i - 1 - p[i] >= 0
                and trans[i+1+p[i]] == trans[i-1-p[i]]
            ):
                p[i] += 1

            if i + p[i] > r:
                c, r = i, p[i]
        
        return sum((val + 1) >> 1 for val in p)