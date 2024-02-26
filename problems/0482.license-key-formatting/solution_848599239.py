# 0482 - License Key Formatting
# Date: 2022-11-23
# Runtime: 132 ms, Memory: 14.7 MB
# Submission Id: 848599239


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        
        count = sum(ch != '-' for ch in s) % k        
        ans = []
        for i in range(n):
            if s[i] == '-':
                continue
            if count == 0:
                if ans: ans.append('-')
                count = k
            ans.append(s[i])
            count -= 1
        return ''.join(ans).upper()