# 0072 - Edit Distance
# Date: 2024-05-26
# Runtime: 73 ms, Memory: 18.6 MB
# Submission Id: 1268316554


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        @cache
        def dp(i, j):
            if i == n1 and j == n2:
                return 0
            if i == n1:
                return n2 - j
            if j == n2:
                return n1 - i
            
            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            return 1 + min(
                dp(i+1, j+1),  # replace
                dp(i+1, j),    # delete
                dp(i, j+1),    # insert
            )

        return dp(0, 0)