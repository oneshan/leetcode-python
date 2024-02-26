# 0472 - Concatenated Words
# Date: 2023-01-27
# Runtime: 959 ms, Memory: 16.6 MB
# Submission Id: 886302546


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        ans = []
        for word in words:
            length = len(word)
            dp = [False] * (length + 1)
            dp[0] = True
            
            for i in range(1, length):
                for j in range(i):
                    dp[i] |= dp[j] and word[j:i] in words

            for j in range(1, length):
                dp[-1] |= dp[j] and word[j:] in words
            
            if dp[-1]:
                ans.append(word)
                
        return ans