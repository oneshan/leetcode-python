# 2338 - Minimum Consecutive Cards to Pick Up
# Date: 2022-09-28
# Runtime: 2222 ms, Memory: 33.4 MB
# Submission Id: 810560772


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        ans = len(cards) + 1
        for idx, val in enumerate(cards):
            if val in seen:
                ans = min(ans, idx-seen[val]+1)
            seen[val] = idx
        return -1 if ans == len(cards) +1 else ans