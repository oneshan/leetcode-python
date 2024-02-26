# 0045 - Jump Game II
# Date: 2022-10-25
# Runtime: 4104 ms, Memory: 15.7 MB
# Submission Id: 829921202


from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque([(0, 0)])
        seen = {0}
        while queue:
            idx, step = queue.popleft()
            if idx == n-1:
                return step
            
            for next_idx in range(idx+1, min(idx+nums[idx]+1, n)):
                if next_idx not in seen:
                    queue.append((next_idx, step+1))
                    seen.add(next_idx)