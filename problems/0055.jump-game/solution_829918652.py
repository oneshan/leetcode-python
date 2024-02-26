# 0055 - Jump Game
# Date: 2022-10-25
# Runtime: 2800 ms, Memory: 15.9 MB
# Submission Id: 829918652


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack = [0]
        seen = {0}
        n = len(nums)
        while stack:
            idx = stack.pop()
            if idx == n-1:
                return True
            for next_idx in range(idx+1, min(n, idx+nums[idx]+1)):
                if next_idx not in seen:
                    stack.append(next_idx)
                    seen.add(next_idx)
        return False