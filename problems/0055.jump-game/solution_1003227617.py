# 0055 - Jump Game
# Date: 2023-07-25
# Runtime: 495 ms, Memory: 17.6 MB
# Submission Id: 1003227617


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for idx, num in enumerate(nums):
            if max_idx < idx:
                return False
            max_idx = max(max_idx, idx + num)
        return True