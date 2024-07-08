# 1549 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Date: 2024-06-23
# Runtime: 453 ms, Memory: 25.9 MB
# Submission Id: 1297509504


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        d_min = deque()  # mono increasing
        d_max = deque()  # mono decreasing

        ans = left = 0
        for right in range(len(nums)):
            while d_min and nums[d_min[-1]] >= nums[right]:
                d_min.pop()
            d_min.append(right)

            while d_max and nums[d_max[-1]] <= nums[right]:
                d_max.pop()
            d_max.append(right)

            while nums[d_max[0]] - nums[d_min[0]] > limit:
                left += 1
                if d_min[0] < left:
                    d_min.popleft()
                if d_max[0] < left:
                    d_max.popleft()
            
            ans = max(ans, right - left + 1)
        
        return ans