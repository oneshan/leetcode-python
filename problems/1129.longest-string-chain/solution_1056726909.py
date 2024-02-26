# 1129 - Longest String Chain
# Date: 2023-09-23
# Runtime: 133 ms, Memory: 20.3 MB
# Submission Id: 1056726909


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)
        
        @cache
        def recur(word):
            count = 1
            for i in range(len(word)):
                next_word = word[:i] + word[i+1:]
                if next_word in words:
                    count = max(count, 1 + recur(next_word))
            return count
        
        ans = 0
        for word in words:
            ans = max(ans, recur(word))
        return ans