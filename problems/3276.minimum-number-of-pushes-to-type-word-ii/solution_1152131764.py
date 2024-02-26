# 3276 - Minimum Number of Pushes to Type Word II
# Date: 2024-01-21
# Runtime: 153 ms, Memory: 17.6 MB
# Submission Id: 1152131764


from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        
        ans = 0
        for idx, value in enumerate(sorted(counter.values(), reverse=True)):
            ans += value * (1 + (idx // 8))
        return ans