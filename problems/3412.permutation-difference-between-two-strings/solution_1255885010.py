# 3412 - Permutation Difference between Two Strings
# Date: 2024-05-12
# Runtime: 41 ms, Memory: 16.5 MB
# Submission Id: 1255885010


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        table = defaultdict(int)
        for idx, ch in enumerate(s):
            table[ch] = idx
        
        ans = 0
        for idx, ch in enumerate(t):
            ans += abs(idx - table[ch])
        return ans