# 0876 - Hand of Straights
# Date: 2024-06-06
# Runtime: 160 ms, Memory: 18.2 MB
# Submission Id: 1279255758


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counter = Counter(hand)

        for num in sorted(counter):
            if counter[num] == 0:
                continue
            diff = counter[num]
            for i in range(groupSize):
                counter[num+i] -= diff
                if counter[num+i] < 0:
                    return False
        return True