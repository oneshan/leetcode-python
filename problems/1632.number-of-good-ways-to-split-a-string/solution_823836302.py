# 1632 - Number of Good Ways to Split a String
# Date: 2022-10-17
# Runtime: 366 ms, Memory: 16.3 MB
# Submission Id: 823836302


class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        prefix = [0] * n
        suffix = [0] * n
        unique = set()
        ans = 0
        
        for i in range(n-1):
            unique.add(s[i])
            prefix[i] = len(unique)
            
        unique.clear()
        for i in range(n-1, 0, -1):
            unique.add(s[i])
            suffix[i] = len(unique)
            
        for i in range(n-1):
            if prefix[i] == suffix[i+1]:
                ans += 1

        return ans