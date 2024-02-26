# 0055 - Jump Game
# Date: 2022-10-24
# Runtime: 532 ms, Memory: 15.2 MB
# Submission Id: 829289371


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = 0
        for idx, num in enumerate(nums):
            if idx > max_len:
                return False
            max_len = max(max_len, idx+num)
        return True