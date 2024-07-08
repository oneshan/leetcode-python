# 0055 - Jump Game
# Date: 2024-05-23
# Runtime: 373 ms, Memory: 17.8 MB
# Submission Id: 1265385763


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_max = 0
        for i in range(n):
            if i > curr_max:
                return False
            curr_max = max(curr_max, i + nums[i])
        return True