# 0876 - Hand of Straights
# Date: 2024-05-23
# Runtime: 162 ms, Memory: 18.5 MB
# Submission Id: 1265716698


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counter = Counter(hand)
        heap = list(counter.keys())
        heapq.heapify(heap)

        while heap:
            card = heapq.heappop(heap)
            if counter[card] == 0:
                continue
            cnt = counter.pop(card)
            for i in range(1, groupSize):
                if counter[card+i] < cnt:
                    return False
                counter[card+i] -= cnt
        return True