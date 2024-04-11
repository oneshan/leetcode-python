# 0987 - Reveal Cards In Increasing Order
# Date: 2024-04-10
# Runtime: 36 ms, Memory: 16.9 MB
# Submission Id: 1228159081


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # sort deck
        deck.sort()

        # gen index
        n = len(deck)
        queue = deque(range(n))
        arr = []
        while queue:
            arr.append(queue.popleft())
            if queue:
                queue.append(queue.popleft())

        ans = [0] * n
        for i in range(n):
            ans[arr[i]] = deck[i]
            
        return ans