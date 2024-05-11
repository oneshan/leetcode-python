# 0239 - Sliding Window Maximum
# Date: 2024-05-10
# Runtime: 1094 ms, Memory: 32.4 MB
# Submission Id: 1254556756


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        queue = deque() # mono decreasing
        for i in range(k):
            while queue and nums[i] >= queue[-1][0]:
                queue.pop()
            queue.append((nums[i], i))

        ans = [queue[0][0]]
        for i in range(k, n):
            while queue and nums[i] >= queue[-1][0]:
                queue.pop()
            queue.append((nums[i], i))
            if queue[0][1] <= i - k:
                queue.popleft()
            ans.append(queue[0][0])

        return ans