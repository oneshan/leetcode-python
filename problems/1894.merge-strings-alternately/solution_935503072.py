# 1894 - Merge Strings Alternately
# Date: 2023-04-18
# Runtime: 35 ms, Memory: 13.9 MB
# Submission Id: 935503072


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        min_len = min(len1,len2)
        
        ans = [None] * (min_len * 2)
        idx = 0
        for c1, c2 in zip(word1, word2):
            ans[idx], ans[idx+1] = c1, c2
            idx += 2
        
        return ''.join(ans) + word1[min_len:] + word2[min_len:]