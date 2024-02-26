# 3296 - Minimum Time to Revert Word to Initial State II
# Date: 2024-02-06
# Runtime: 407 ms, Memory: 58.2 MB
# Submission Id: 1167486853


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

        start = (n - lps[-1])
        start -= start % k
        for i in range(start, n, k):
            if word[0] == word[i] and word[i:] == word[:-i]:
                return i // k
        return ceil(n / k)