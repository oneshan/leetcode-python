# 1885 - Count Number of Homogenous Substrings
# Date: 2023-11-09
# Runtime: 97 ms, Memory: 17.3 MB
# Submission Id: 1095128141


class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 1_000_000_007
        
        ans = 0
        prev_ch, count = '', 0
        for ch in s:
            if prev_ch != ch:
                prev_ch, count = ch, 1
            else:
                count += 1
            ans = (ans + count) % MOD
        
        return ans