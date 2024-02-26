# 1056 - Capacity To Ship Packages Within D Days
# Date: 2023-02-22
# Runtime: 607 ms, Memory: 17.2 MB
# Submission Id: 902605185


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(capacity):
            curr_weight, curr_days = 0, 1
            for weight in weights:
                curr_weight += weight
                if curr_weight > capacity:
                    curr_weight = weight
                    curr_days += 1
                    if curr_days > days:
                        return False
            return True
        
        left = right = 0
        for weight in weights:
            left = max(left, weight)
            right += weight
        
        while left < right:
            mid = (left + right) // 2
            if valid(mid):
                right = mid
            else:
                left = mid + 1
        return left