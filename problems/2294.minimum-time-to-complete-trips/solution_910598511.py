# 2294 - Minimum Time to Complete Trips
# Date: 2023-03-07
# Runtime: 2877 ms, Memory: 28.4 MB
# Submission Id: 910598511


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def calculate(unit):
            total = 0
            for t in time:
                total += (unit // t)
            return total
        
        left, right = 1, max(time) * totalTrips
        while left < right:
            mid = (left + right) // 2
            if calculate(mid) >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return left