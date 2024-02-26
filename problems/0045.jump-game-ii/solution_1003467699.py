# 0045 - Jump Game II
# Date: 2023-07-25
# Runtime: 1463 ms, Memory: 18 MB
# Submission Id: 1003467699


from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        seen = {0}
        queue = deque([0])
        step = 0
        while queue:
            for _ in range(len(queue)):
                idx = queue.popleft()
                if idx == n-1:
                    return step
                for next_idx in range(idx+1, min(n, idx+1+nums[idx])):
                    if next_idx not in seen:
                        seen.add(next_idx)
                        queue.append(next_idx)
            step += 1
                