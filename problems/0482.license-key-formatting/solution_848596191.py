# 0482 - License Key Formatting
# Date: 2022-11-23
# Runtime: 124 ms, Memory: 15.4 MB
# Submission Id: 848596191


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        ans, curr = [], 0
        for i in range(n-1, -1, -1):
            if s[i] == '-':
                continue
            if curr == k:
                ans.append('-')
                curr = 0
                
            ans.append(s[i])
            curr += 1
        return ''.join(ans[::-1]).upper()