# 3233 - Maximize the Number of Partitions After Operations
# Date: 2024-01-07
# Runtime: 1042 ms, Memory: 217.9 MB
# Submission Id: 1139341980


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        if k == 26:
            return 1
        
        @cache
        def dp(idx, mask, used):
            if idx == n:
                return 0
            
            curr = 1 << (ord(s[idx]) - ord('a'))
            new_mask = mask | curr
            if bin(new_mask).count('1') <= k:
                res = dp(idx+1, new_mask, used)
            else:
                res = 1 + dp(idx+1, curr, used)
                
            if not used:
                for ch in range(26):
                    curr = 1 << ch
                    new_mask = mask | curr
                    if bin(new_mask).count('1') <= k:
                        res = max(res, dp(idx+1, new_mask, True))
                    else:
                        res = max(res, 1 + dp(idx+1, curr, True))
            
            return res
        
        return 1 + dp(0, 0, False)