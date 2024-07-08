# 2292 - Counting Words With a Given Prefix
# Date: 2024-06-03
# Runtime: 38 ms, Memory: 16.6 MB
# Submission Id: 1275858631


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)