# 0239 - Sliding Window Maximum
# Date: 2024-05-28
# Runtime: 1096 ms, Memory: 33.2 MB
# Submission Id: 1270332085


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        queue = deque() # mono decreasing (num, idx)

        ans = []
        for i in range(n):
            while queue and nums[i] >= queue[-1][0]:
                queue.pop()
            queue.append((nums[i], i))
            if queue[0][1] <= i - k:
                queue.popleft()
            if i >= k-1:
                ans.append(queue[0][0])

        return ans