# 2868 - Continuous Subarrays
# Date: 2024-03-26
# Runtime: 610 ms, Memory: 27.2 MB
# Submission Id: 1214122019


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
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
             
            while nums[d_max[0]] - nums[d_min[0]] > 2:
                left += 1
                if left > d_min[0]:
                    d_min.popleft()
                if left > d_max[0]:
                    d_max.popleft()
            
            ans += right - left + 1

        return ans