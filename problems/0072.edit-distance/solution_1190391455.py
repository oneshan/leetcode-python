# 0072 - Edit Distance
# Date: 2024-03-01
# Runtime: 70 ms, Memory: 18.4 MB
# Submission Id: 1190391455


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        @cache
        def recur(p1, p2):
            if p1 == -1:
                return p2 + 1
            if p2 == -1:
                return p1 + 1
            if word1[p1] == word2[p2]:
                return recur(p1-1, p2-1)
            return 1 + min(
                recur(p1-1, p2-1),
                recur(p1-1, p2),
                recur(p1, p2-1),
            )

        return recur(len(word1)-1, len(word2)-1) 