# 0876 - Hand of Straights
# Date: 2024-06-06
# Runtime: 164 ms, Memory: 18.5 MB
# Submission Id: 1279262311


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counter = Counter(hand)
        for card in hand:
            i = card
            while counter[i-1]:
                i -= 1
            
            while i <= card:
                while counter[i]:
                    for next_card in range(i, i+groupSize):
                        if not counter[next_card]:
                            return False
                        counter[next_card] -= 1
                i += 1
        
        return True