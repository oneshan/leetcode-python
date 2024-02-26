# 1549 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Date: 2023-09-11
# Runtime: 536 ms, Memory: 25.8 MB
# Submission Id: 1046374450


from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = left = 0
        d_min = deque()  # mono-increasing
        d_max = deque()  # mono-decreasing
        for right, num in enumerate(nums):
            while d_min and nums[d_min[-1]] > num:
                d_min.pop()
            d_min.append(right)
            
            while d_max and nums[d_max[-1]] < num:
                d_max.pop()
            d_max.append(right)
             
            while nums[d_max[0]] - nums[d_min[0]] > limit:
                left += 1
                if left > d_min[0]:
                    d_min.popleft()
                if left > d_max[0]:
                    d_max.popleft()
            
            ans = max(ans, right - left + 1)

        return ans