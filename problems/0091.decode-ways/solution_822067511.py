# 0091 - Decode Ways
# Date: 2022-10-14
# Runtime: 47 ms, Memory: 14.1 MB
# Submission Id: 822067511


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        memo = {}
        def dfs(idx):
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0
            if idx == len(s)-1:
                return 1

            if idx not in memo:
                count = dfs(idx+1)
                if s[idx] == '1' or (s[idx] =='2' and s[idx+1] <= '6'):
                    count += dfs(idx+2)
                memo[idx] = count
            return memo[idx]
        
        return dfs(0)
        