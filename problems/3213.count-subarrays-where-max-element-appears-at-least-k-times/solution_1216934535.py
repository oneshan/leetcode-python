# 3213 - Count Subarrays Where Max Element Appears at Least K Times
# Date: 2024-03-29
# Runtime: 886 ms, Memory: 30.8 MB
# Submission Id: 1216934535


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        ans = 0
        queue = deque()
        for right, num in enumerate(nums):
            if num == max_num:
                queue.append(right)
            if len(queue) < k:
                continue
            if len(queue) == k+1:
                queue.popleft()
            ans += queue[0] + 1
        return ans