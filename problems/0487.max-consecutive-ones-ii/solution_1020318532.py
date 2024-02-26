# 0487 - Max Consecutive Ones II
# Date: 2023-08-13
# Runtime: 317 ms, Memory: 16.6 MB
# Submission Id: 1020318532


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pre_zero = curr_zero = -1
        ans = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                pre_zero, curr_zero = curr_zero, idx
            ans = max(ans, idx - pre_zero)
        return ans