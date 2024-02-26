# 0907 - Koko Eating Bananas
# Date: 2023-09-18
# Runtime: 387 ms, Memory: 17.8 MB
# Submission Id: 1051903709


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        
        def check(speed):
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / speed)
                if hour > h:
                    return False
            return True
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left