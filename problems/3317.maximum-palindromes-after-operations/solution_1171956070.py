# 3317 - Maximum Palindromes After Operations
# Date: 2024-02-11
# Runtime: 187 ms, Memory: 17.3 MB
# Submission Id: 1171956070


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        char_freq = Counter()
        pairs = []

        for word in words:
            pairs.append(len(word) >> 1)
            for char in word:
                char_freq[char] += 1

        total = sum(freq >> 1 for freq in char_freq.values())
        pairs.sort()

        idx = 0
        for pair in pairs:
            if total - pair < 0:
                return idx
            total -= pair
            idx += 1

        return len(pairs)