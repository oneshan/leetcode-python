# 0876 - Hand of Straights
# Date: 2024-05-23
# Runtime: 148 ms, Memory: 18.1 MB
# Submission Id: 1265720539


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counter = Counter(hand)
        queue = deque()

        prev, required_cnt = -1, 0
        for card in sorted(counter):
            if required_cnt > counter[card]:
                return False
            if required_cnt > 0 and card > prev + 1:
                return False

            queue.append(counter[card] - required_cnt)
            prev, required_cnt = card, counter[card]
            if len(queue) == groupSize:
                required_cnt -= queue.popleft()

        return required_cnt == 0