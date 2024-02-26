# 1744 - Number of Ways to Form a Target String Given a Dictionary
# Date: 2023-04-16
# Runtime: 1942 ms, Memory: 20.5 MB
# Submission Id: 934553594


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        len_w = len(words[0])
        
        count = [[0] * 26 for _ in range(len_w)]
        for word in words:
            for idx, ch in enumerate(word):
                count[idx][ord(ch) - ord('a')] += 1
        
        dp = [1] * (len_w + 1)
        dp[0], prev = 0, 1
        for ch in target:
            for idx in range(len_w):
                dp[idx+1], prev = (dp[idx] + prev * count[idx][ord(ch)-ord('a')]) % mod, dp[idx+1]
            prev = 0
        
        return dp[-1]