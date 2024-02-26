# 3309 - Count Prefix and Suffix Pairs I
# Date: 2024-02-18
# Runtime: 48 ms, Memory: 16.6 MB
# Submission Id: 1178390595


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            size = len(words[i])
            for j in range(i+1, n):
                if words[j][:size] == words[i] and words[j][-size:] == words[i]:
                    ans += 1
        return ans