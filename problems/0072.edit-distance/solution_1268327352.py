# 0072 - Edit Distance
# Date: 2024-05-26
# Runtime: 80 ms, Memory: 16.5 MB
# Submission Id: 1268327352


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        dp = [0] * (n2+1)
        for j in range(n2+1):
            dp[j] = j
        
        for i in range(n1):
            next_dp = [0] * (n2+1)
            next_dp[0] = i + 1
            for j in range(n2):
                if word1[i] == word2[j]:
                    next_dp[j+1] = dp[j]
                else:
                    next_dp[j+1] = 1 + min(
                        next_dp[j],  # insert
                        dp[j],    # replace
                        dp[j+1],  # delete
                    )
            dp = next_dp
            
        return dp[-1]