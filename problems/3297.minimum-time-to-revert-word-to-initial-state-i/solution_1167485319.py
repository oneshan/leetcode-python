# 3297 - Minimum Time to Revert Word to Initial State I
# Date: 2024-02-06
# Runtime: 32 ms, Memory: 16.6 MB
# Submission Id: 1167485319


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        count = 1
        for i in range(k, n, k):
            if word[i] == word[0] and word[i:] == word[:-i]:
                return count
            count += 1
        return count