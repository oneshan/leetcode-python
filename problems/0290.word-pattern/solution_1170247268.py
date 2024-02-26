# 0290 - Word Pattern
# Date: 2024-02-09
# Runtime: 32 ms, Memory: 16.6 MB
# Submission Id: 1170247268


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        p2s, s2p = {}, {}
        for ch, word in zip(pattern, words):
            if ch in p2s and p2s[ch] != word:
                return False
            if word in s2p and s2p[word] != ch:
                return False
            p2s[ch] = word
            s2p[word] = ch
        return True