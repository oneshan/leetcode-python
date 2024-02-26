# 0209 - Minimum Size Subarray Sum
# Date: 2024-02-22
# Runtime: 179 ms, Memory: 30.4 MB
# Submission Id: 1182687755


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        left = curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0
            