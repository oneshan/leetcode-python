# 2102 - Find the Middle Index in Array
# Date: 2022-07-11
# Runtime: 38 ms, Memory: 13.9 MB
# Submission Id: 744035502


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for idx, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return idx
            left_sum += num
        return -1