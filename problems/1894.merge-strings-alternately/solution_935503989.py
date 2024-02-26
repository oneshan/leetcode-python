# 1894 - Merge Strings Alternately
# Date: 2023-04-18
# Runtime: 36 ms, Memory: 13.8 MB
# Submission Id: 935503989


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        ans = [None] * (len1 + len2)
        p1 = p2 = 0
        
        idx = 0
        for _ in range(len1+len2):
            if p1 < len1:
                ans[idx] = word1[p1]
                p1 += 1
                idx += 1
            if p2 < len2:
                ans[idx] = word2[p2]
                p2 += 1
                idx += 1
        return ''.join(ans)