# 0987 - Reveal Cards In Increasing Order
# Date: 2024-04-10
# Runtime: 41 ms, Memory: 16.9 MB
# Submission Id: 1228159855


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        n = len(deck)
        queue = deque(range(n))
        
        ans = [0] * n
        for card in deck:
            ans[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())

        return ans