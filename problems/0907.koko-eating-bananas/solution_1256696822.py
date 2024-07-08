# 0907 - Koko Eating Bananas
# Date: 2024-05-13
# Runtime: 266 ms, Memory: 18.2 MB
# Submission Id: 1256696822


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        def check(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)
                if time > h:
                    return False
            return True

        left, right = 1, 1_000_000_000
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left