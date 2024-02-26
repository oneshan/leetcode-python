# 3297 - Minimum Time to Revert Word to Initial State I
# Date: 2024-02-05
# Runtime: 31 ms, Memory: 16.8 MB
# Submission Id: 1166661667


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

        for i in range(n - lps[n-1], n):
            if i % k == 0 and word[0] == word[i] and word[:n-i] == word[i:n]:
                return i // k

        return ceil(n / k)