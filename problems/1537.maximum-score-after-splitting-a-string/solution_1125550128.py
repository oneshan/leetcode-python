# 1537 - Maximum Score After Splitting a String
# Date: 2023-12-22
# Runtime: 26 ms, Memory: 17.1 MB
# Submission Id: 1125550128


class Solution:
    def maxScore(self, s: str) -> int:
        ones = sum(ch == '1' for ch in s)
        n = len(s)
        
        ans = zeros = 0
        for i in range(n-1):
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1    
            ans = max(ans, zeros + ones)
                        
        return ans