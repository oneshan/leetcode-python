# 2044 - Number of Wonderful Substrings
# Date: 2024-04-30
# Runtime: 1430 ms, Memory: 17.4 MB
# Submission Id: 1245450832


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = defaultdict(int)
        freq[0] = 1

        mask = ans = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            ans += freq[mask]

            for i in range(10):
                one_odd = mask ^ (1 << i)
                ans += freq[one_odd]

            freq[mask] += 1
        
        return ans