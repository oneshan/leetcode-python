# 0140 - Word Break II
# Date: 2022-10-30
# Runtime: 73 ms, Memory: 13.9 MB
# Submission Id: 833045677


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def backtrack(i, words):
            if i == len(s):
                ans.append(' '.join(words))
                return

            for word in wordDict:
                if s[i:i+len(word)] == word:
                    words.append(word)
                    backtrack(i+len(word), words)
                    words.pop()

        backtrack(0, [])
        return ans