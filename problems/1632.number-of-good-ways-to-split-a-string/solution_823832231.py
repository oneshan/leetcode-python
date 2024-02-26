# 1632 - Number of Good Ways to Split a String
# Date: 2022-10-17
# Runtime: 524 ms, Memory: 14.6 MB
# Submission Id: 823832231


class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) == 1:
            return 0
        
        table_l = {}
        table_r = {}
        for i in range(len(s)):
            table_r[s[i]] = table_r.get(s[i], 0) + 1
        
        ans = 0
        for i in range(len(s)-1):
            table_l[s[i]] = table_l.get(s[i], 0) + 1
            if table_r[s[i]] == 1:
                table_r.pop(s[i])
            else:
                table_r[s[i]] -= 1
        
            if len(table_l) == len(table_r):
                ans += 1
        return ans