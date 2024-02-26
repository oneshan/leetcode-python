# 0139 - Word Break
# Date: 2022-10-29
# Runtime: 48 ms, Memory: 13.9 MB
# Submission Id: 832757428


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]