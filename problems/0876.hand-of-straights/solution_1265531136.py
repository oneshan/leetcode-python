# 0876 - Hand of Straights
# Date: 2024-05-23
# Runtime: 162 ms, Memory: 18.2 MB
# Submission Id: 1265531136


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counter = Counter(hand)
        for card in sorted(counter.keys()):
            count = counter[card]
            if count == 0:
                continue
            for i in range(groupSize):
                if counter[card+i] < count:
                    return False
                counter[card+i] -= count

        return True