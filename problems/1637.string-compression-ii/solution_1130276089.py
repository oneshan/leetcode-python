# 1637 - String Compression II
# Date: 2023-12-28
# Runtime: 1149 ms, Memory: 21.2 MB
# Submission Id: 1130276089


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        comp = lambda x: 1 if x < 2 else 2 if x < 10 else 3 if x < 100 else 4
        
        @cache
        def dp(idx, k):
            if k < 0:
                return float('inf')
            if idx < 0:
                return 0
            
            delete_ch = dp(idx-1, k-1)
            keep_ch = float('inf')
            count = 0
            for i in range(idx, -1, -1):
                if s[idx] == s[i]:
                    count += 1
                elif k == 0:
                    break
                else:
                    k -= 1
                keep_ch = min(keep_ch, dp(i-1, k) + comp(count))
            return min(delete_ch, keep_ch)
        
        return dp(len(s)-1, k)