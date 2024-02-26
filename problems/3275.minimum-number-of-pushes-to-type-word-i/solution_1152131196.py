# 3275 - Minimum Number of Pushes to Type Word I
# Date: 2024-01-21
# Runtime: 44 ms, Memory: 16.6 MB
# Submission Id: 1152131196


from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        
        ans = 0
        for idx, value in enumerate(sorted(counter.values(), reverse=True)):
            ans += value * (1 + (idx // 8))
        return ans