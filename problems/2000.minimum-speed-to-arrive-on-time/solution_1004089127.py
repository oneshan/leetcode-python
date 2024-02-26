# 2000 - Minimum Speed to Arrive on Time
# Date: 2023-07-26
# Runtime: 4926 ms, Memory: 30.8 MB
# Submission Id: 1004089127


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1
        
        def time_required(speed):
            total = 0
            for i in range(n-1):
                total += int((dist[i] + speed - 1) / speed)
            total += dist[-1] / speed
            return total
        
        ans = -1
        left, right = 1, 1000_000_000
        while left < right:
            mid = (left + right) // 2
            if time_required(mid) <= hour:
                right = mid
            else:
                left = mid + 1
        return right