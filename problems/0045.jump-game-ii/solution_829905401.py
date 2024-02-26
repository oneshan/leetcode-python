# 0045 - Jump Game II
# Date: 2022-10-25
# Runtime: 317 ms, Memory: 15.1 MB
# Submission Id: 829905401


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count, curr_jump_end, max_jump_end = 0, 0, 0
        for idx, num in enumerate(nums):
            if idx > curr_jump_end:
                count += 1
                curr_jump_end = max_jump_end
            max_jump_end = max(max_jump_end, idx + num)
        return count