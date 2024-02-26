# 2338 - Minimum Consecutive Cards to Pick Up
# Date: 2023-08-23
# Runtime: 691 ms, Memory: 35.7 MB
# Submission Id: 1029598095


from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = defaultdict(int)
        ans = float('inf')
        for idx, card in enumerate(cards):
            if card in last_seen:
                ans = min(ans, idx - last_seen[card] + 1)
            last_seen[card] = idx
        return ans if ans < float('inf') else -1