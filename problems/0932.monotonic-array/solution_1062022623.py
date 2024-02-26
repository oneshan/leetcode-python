# 0932 - Monotonic Array
# Date: 2023-09-29
# Runtime: 777 ms, Memory: 30.3 MB
# Submission Id: 1062022623


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_desc = is_incr = False
        prev = nums[0]
        for num in nums:
            if prev == num:
                continue
            if prev > num:
                if is_incr:
                    return False
                is_desc = True
            else:
                if is_desc:
                    return False
                is_incr = True
            prev = num
        return True