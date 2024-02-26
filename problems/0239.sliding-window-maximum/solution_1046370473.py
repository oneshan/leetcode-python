# 0239 - Sliding Window Maximum
# Date: 2023-09-11
# Runtime: 1264 ms, Memory: 33.3 MB
# Submission Id: 1046370473


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()  # mono-decreasing
        for idx, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(idx)
            if queue[0] == idx - k:
                queue.popleft()
            if idx >= k-1:
                ans.append(nums[queue[0]])
        return ans