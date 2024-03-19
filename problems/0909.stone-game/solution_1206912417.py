# 0909 - Stone Game
# Date: 2024-03-18
# Runtime: 422 ms, Memory: 126.8 MB
# Submission Id: 1206912417


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def recur(left, right):
            if left > right:
                return 0

            is_alice = (left + right) & 1
            if is_alice:
                return max(
                    piles[left] + recur(left+1, right),
                    piles[right] + recur(left, right-1)
                )
            return min(
                -piles[left] + recur(left+1, right),
                -piles[right] + recur(left, right-1)
            )

        return recur(0, len(piles)-1) > 0