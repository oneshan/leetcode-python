# 0907 - Koko Eating Bananas
# Date: 2023-03-08
# Runtime: 460 ms, Memory: 15.5 MB
# Submission Id: 911271511


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            hour = 0
            for pile in piles:
                hour += (pile-1) // k + 1
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