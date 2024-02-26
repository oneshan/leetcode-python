# 0907 - Koko Eating Bananas
# Date: 2022-10-12
# Runtime: 1641 ms, Memory: 15.2 MB
# Submission Id: 820869278


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hour = 0
            for pile in piles:
                dh, r = divmod(pile, k)
                hour += dh + (r > 0)
                if hour > h:
                    return False
            return True
        
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left