# 1441 - Minimum Flips to Make a OR b Equal to c
# Date: 2023-06-08
# Runtime: 48 ms, Memory: 16.2 MB
# Submission Id: 966221985


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        num = (a | b) ^ c
        while num:
            ans += 1
            num &= num-1
        
        num = (a & b) & ((a | b) ^ c)
        while num:
            ans += 1
            num &= num-1
            
        return ans