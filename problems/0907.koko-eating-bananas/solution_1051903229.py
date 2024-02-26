# 0907 - Koko Eating Bananas
# Date: 2023-09-18
# Runtime: 415 ms, Memory: 17.9 MB
# Submission Id: 1051903229


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        
        def check(speed):
            hour = 0
            for pile in piles:
                r, c = divmod(pile, speed)
                hour += r + bool(c)
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