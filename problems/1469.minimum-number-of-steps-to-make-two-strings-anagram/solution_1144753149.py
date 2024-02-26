# 1469 - Minimum Number of Steps to Make Two Strings Anagram
# Date: 2024-01-13
# Runtime: 101 ms, Memory: 17.7 MB
# Submission Id: 1144753149


from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        ans = 0
        for ch in c1:
            ans += max(c1[ch] - c2[ch], 0)
        return ans