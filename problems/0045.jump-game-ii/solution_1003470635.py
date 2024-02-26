# 0045 - Jump Game II
# Date: 2023-07-25
# Runtime: 140 ms, Memory: 17.3 MB
# Submission Id: 1003470635


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_end = curr_end = step = 0
        for i in range(len(nums)-1):
            max_end = max(max_end, i + nums[i])
            if curr_end == i:
                step += 1
                curr_end = max_end
        return step