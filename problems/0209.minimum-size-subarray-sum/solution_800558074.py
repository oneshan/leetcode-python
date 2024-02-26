# 0209 - Minimum Size Subarray Sum
# Date: 2022-09-15
# Runtime: 621 ms, Memory: 27.1 MB
# Submission Id: 800558074


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr_sum = 0
        ans = len(nums) + 1
        for right, num in enumerate(nums):
            curr_sum += num
            while left < right and curr_sum - nums[left] >= target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum >= target:
                ans = min(right-left+1, ans)
        return ans if ans <= len(nums) else 0