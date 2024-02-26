# 1056 - Capacity To Ship Packages Within D Days
# Date: 2023-02-22
# Runtime: 706 ms, Memory: 17.1 MB
# Submission Id: 902603894


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(capacity):
            curr_weight, curr_days = 0, 1
            for weight in weights:
                if weight > capacity:
                    return False
                curr_weight += weight
                if curr_weight > capacity:
                    curr_weight = weight
                    curr_days += 1
                    if curr_days > days:
                        return False
            return True
        
        left, right = 1, sum(weights)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if valid(mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans