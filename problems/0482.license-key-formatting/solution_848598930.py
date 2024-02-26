# 0482 - License Key Formatting
# Date: 2022-11-23
# Runtime: 195 ms, Memory: 14.6 MB
# Submission Id: 848598930


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        
        total_char = 0
        for ch in s:
            if ch != '-':
                total_char += 1
        
        ans = []
        count = total_char % k
        for i in range(n):
            if s[i] == '-':
                continue
            if count == 0:
                if ans: ans.append('-')
                count = k
            ans.append(s[i])
            count -= 1
        return ''.join(ans).upper()