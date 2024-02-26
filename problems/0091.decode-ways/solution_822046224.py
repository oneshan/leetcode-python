# 0091 - Decode Ways
# Date: 2022-10-14
# Runtime: 48 ms, Memory: 13.8 MB
# Submission Id: 822046224


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        two_back = one_back = 1
        for i in range(1, len(s)):
            curr = 0
            if s[i] != '0':
                curr += one_back
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                curr += two_back
            two_back, one_back = one_back, curr
            
        return one_back