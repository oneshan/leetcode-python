# 0139 - Word Break
# Date: 2022-10-30
# Runtime: 84 ms, Memory: 14 MB
# Submission Id: 832780853


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