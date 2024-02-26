# 1632 - Number of Good Ways to Split a String
# Date: 2022-10-17
# Runtime: 390 ms, Memory: 14.7 MB
# Submission Id: 824394625


class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        prefix = 0
        unique_prefix = 0
        suffix = {}
        ans = 0
        
        suffix = {}
        for i in range(n):
            suffix[s[i]] = suffix.get(s[i], 0) + 1
                    
        for i in range(n-1):
            mask = 1 << (ord(s[i])-97)
            if mask & prefix == 0:
                unique_prefix += 1
                prefix |= mask
            if suffix[s[i]] == 1:
                suffix.pop(s[i])
            else:
                suffix[s[i]] -= 1
            
            if unique_prefix == len(suffix):
                ans += 1

        return ans