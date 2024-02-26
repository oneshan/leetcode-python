# 0239 - Sliding Window Maximum
# Date: 2022-10-01
# Runtime: 1787 ms, Memory: 29.8 MB
# Submission Id: 812680820


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * (len(nums)-k+1)

        queue = deque()
        for idx in range(len(nums)):
            
            # clean deque
            if queue and queue[0] + k == idx:
                queue.popleft()
            while queue and nums[idx] > nums[queue[-1]]:
                queue.pop()
            
            # append the current element to the deque
            queue.append(idx)
            
            if idx + 1 >= k:
                ans[idx+1-k] = nums[queue[0]]

        return ans