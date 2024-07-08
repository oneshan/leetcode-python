# 0876 - Hand of Straights
# Date: 2024-05-23
# Runtime: 170 ms, Memory: 18.3 MB
# Submission Id: 1265736682


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counter = Counter(hand)
        heap = list(counter.keys())
        heapq.heapify(heap)

        while heap:
            card = heap[0]
            if counter[card] == 0:
                heapq.heappop(heap)
                continue

            for i in range(groupSize):
                if counter[card+i] == 0:
                    return False
                counter[card+i] -= 1
        return True