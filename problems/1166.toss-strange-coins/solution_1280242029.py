# 1166 - Toss Strange Coins
# Date: 2024-06-07
# Runtime: 1454 ms, Memory: 521.2 MB
# Submission Id: 1280242029


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        @cache
        def recur(i, head):
            if i == len(prob):
                return head == target
            if head > target:
                return 0            
            return (
                prob[i] * recur(i+1, head + 1)
                + (1-prob[i]) * recur(i+1, head)
            )

        return recur(0, 0)