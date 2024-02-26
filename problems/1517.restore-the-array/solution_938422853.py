# 1517 - Restore The Array
# Date: 2023-04-23
# Runtime: 1000 ms, Memory: 17.9 MB
# Submission Id: 938422853


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [0] * (n+1)
        dp[-1] = 1
        
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue
            res = num = 0
            for j in range(i, n):
                num = num * 10 + ord(s[j]) - ord('0')
                if num > k:
                    break
                res += dp[j+1]
            dp[i] = res % mod
        
        return dp[0]