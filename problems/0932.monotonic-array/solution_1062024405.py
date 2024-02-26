# 0932 - Monotonic Array
# Date: 2023-09-29
# Runtime: 833 ms, Memory: 30.5 MB
# Submission Id: 1062024405


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_desc = is_incr = True
        prev = nums[0]
        for num in nums:
            if prev == num:
                continue
            if prev > num:
                is_incr = False
            else:
                is_desc = False
            prev = num
        return is_desc or is_incr