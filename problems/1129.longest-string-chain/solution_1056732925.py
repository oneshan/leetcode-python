# 1129 - Longest String Chain
# Date: 2023-09-23
# Runtime: 162 ms, Memory: 18.4 MB
# Submission Id: 1056732925


from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        dp = defaultdict(int)
        
        ans = 0
        for word in words:
            curr_len = 1
            for i in range(len(word)):
                next_word = word[:i] + word[i+1:]
                curr_len = max(curr_len, 1 + dp[next_word])
            dp[word] = curr_len
            ans = max(ans, curr_len)
        return ans