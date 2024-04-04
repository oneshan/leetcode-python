# 0713 - Subarray Product Less Than K
# Date: 2024-03-27
# Runtime: 495 ms, Memory: 19.3 MB
# Submission Id: 1215039293


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, curr, ans = 0, 1, 0
        for right, num in enumerate(nums):
            curr *= num
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1
        return ans