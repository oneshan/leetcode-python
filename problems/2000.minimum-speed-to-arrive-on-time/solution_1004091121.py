# 2000 - Minimum Speed to Arrive on Time
# Date: 2023-07-26
# Runtime: 3572 ms, Memory: 31 MB
# Submission Id: 1004091121


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1
        
        def is_valid(speed):
            total = 0
            for d in dist:
                total = ceil(total)
                total += (d / speed)
                if total > hour:
                    return False
            return True
        
        ans = -1
        left, right = 1, 1000_000_000
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        return right