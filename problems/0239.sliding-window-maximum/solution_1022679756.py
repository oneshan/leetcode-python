# 0239 - Sliding Window Maximum
# Date: 2023-08-16
# Runtime: 1334 ms, Memory: 32.7 MB
# Submission Id: 1022679756


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        n = len(nums)
        ans = [0] * (n-k+1)
        
        for i in range(n):    
            # clean deque
            if queue and queue[0] + k == i:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            
            # append the current element to the deque
            queue.append(i)
            
            if i + 1 >= k:
                ans[i+1-k] = nums[queue[0]]

        return ans