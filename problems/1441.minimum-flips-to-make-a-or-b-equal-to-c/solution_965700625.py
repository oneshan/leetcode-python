# 1441 - Minimum Flips to Make a OR b Equal to c
# Date: 2023-06-07
# Runtime: 53 ms, Memory: 16.3 MB
# Submission Id: 965700625


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        num = (a | b) ^ c
        while num:
            num &= (num-1)
            ans += 1
        
        num = (a & b)
        while num:
            next_num = num & (num-1)
            num ^= next_num
            if num & c == 0:
                ans += 1
            num = next_num
        
        return ans