# 2000 - Minimum Speed to Arrive on Time
# Date: 2022-10-12
# Runtime: 3974 ms, Memory: 28.8 MB
# Submission Id: 820906341


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1
        
        def is_valid(speed):
            hour_spent = 0
            for d in dist:
                hour_spent = ceil(hour_spent)
                hour_spent += d / speed
                if hour_spent > hour:
                    return False
            return True
        
        left, right = 1, 10 ** 7
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left 