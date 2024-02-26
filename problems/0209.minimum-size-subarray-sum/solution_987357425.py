# 0209 - Minimum Size Subarray Sum
# Date: 2023-07-06
# Runtime: 271 ms, Memory: 29 MB
# Submission Id: 987357425


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr = 0
        ans = float('inf')
        for right in range(len(nums)):
            curr += nums[right]
            while left < right and curr - nums[left] >= target:
                curr -= nums[left]
                left += 1
            if curr >= target:
                ans = min(ans, right - left + 1)
        return ans if ans != float('inf') else 0