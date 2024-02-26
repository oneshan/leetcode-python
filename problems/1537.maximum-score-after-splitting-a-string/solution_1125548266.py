# 1537 - Maximum Score After Splitting a String
# Date: 2023-12-22
# Runtime: 27 ms, Memory: 17.5 MB
# Submission Id: 1125548266


class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        
        best = -inf
        ones = zeros = 0
        for i in range(n-1):
            if s[i] == '1':
                ones += 1
            else:
                zeros += 1    
            best = max(best, zeros - ones)
            
        if s[-1] == '1':
            ones += 1
            
        return best + ones