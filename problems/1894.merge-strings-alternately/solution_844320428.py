# 1894 - Merge Strings Alternately
# Date: 2022-11-16
# Runtime: 56 ms, Memory: 14 MB
# Submission Id: 844320428


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        n1, n2 = len(word1), len(word2)
        ans = [None] * (n1+n2)
        while p1 < n1 or p2 < n2:
            if p1 < n1:
                ans[p1+p2] = word1[p1]
                p1 += 1
            if p2 < n2:
                ans[p1+p2] = word2[p2]
                p2 += 1
        return ''.join(ans)