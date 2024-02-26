# 3296 - Minimum Time to Revert Word to Initial State II
# Date: 2024-02-06
# Runtime: 398 ms, Memory: 58.3 MB
# Submission Id: 1167492606


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        lps = [0] * n

        j = 0
        for i in range(1, n):
            while j and word[i] != word[j]:
                j = lps[j-1]
            if word[i] == word[j]:
                j += 1
                lps[i] = j

        i = lps[-1]
        while i and (n-i) % k:
            i = lps[i-1]
        return ceil((n-i) / k)