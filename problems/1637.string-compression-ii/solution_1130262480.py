# 1637 - String Compression II
# Date: 2023-12-28
# Runtime: 3443 ms, Memory: 371.8 MB
# Submission Id: 1130262480


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @cache
        def dp(idx, k, last_ch, last_count):
            if k < 0:
                return float('inf')
            if idx == n:
                return 0
            
            delete_ch = dp(idx+1, k-1, last_ch, last_count)
            
            if s[idx] == last_ch:
                keep_ch = dp(idx+1, k, s[idx], last_count + 1) + (last_count in [1, 9, 99])
            else:
                keep_ch = dp(idx+1, k, s[idx], 1) + 1
                
            return min(delete_ch, keep_ch)
        
        n = len(s)
        return dp(0, k, '', 0)