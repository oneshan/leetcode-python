# 0713 - Subarray Product Less Than K
# Date: 2022-09-23
# Runtime: 1232 ms, Memory: 16.5 MB
# Submission Id: 806912338


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, curr, ans = 0, 1, 0
        for right in range(len(nums)):
            curr *= nums[right]
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1
        return ans