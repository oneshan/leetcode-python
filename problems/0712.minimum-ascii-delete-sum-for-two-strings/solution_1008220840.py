# 0712 - Minimum ASCII Delete Sum for Two Strings
# Date: 2023-07-31
# Runtime: 911 ms, Memory: 221.7 MB
# Submission Id: 1008220840


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @cache
        def recur(i, j):
            if i < 0 and j < 0:
                return 0
            
            if i < 0:
                return sum(ord(s2[k]) for k in range(j+1))
                        
            if j < 0:
                return sum(ord(s1[k]) for k in range(i+1))       
                        
            if s1[i] == s2[j]:
                return recur(i-1, j-1)
            
            return min(ord(s1[i]) + recur(i-1, j),
                       ord(s2[j]) + recur(i, j-1))

        return recur(len(s1)-1, len(s2)-1)