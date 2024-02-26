# 1894 - Merge Strings Alternately
# Date: 2023-07-26
# Runtime: 47 ms, Memory: 16.4 MB
# Submission Id: 1004442094


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        ans = [None] * (len1 + len2)
        
        idx = 0
        for i in range(max(len1, len2)):
            if i < len1:
                ans[idx] = word1[i]
                idx += 1
            if i < len2:
                ans[idx] = word2[i]
                idx += 1
        return ''.join(ans)