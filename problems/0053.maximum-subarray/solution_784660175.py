# 0053 - Maximum Subarray
# Date: 2022-08-27
# Runtime: 1329 ms, Memory: 27.8 MB
# Submission Id: 784660175


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        current = 0
        for num in nums:
            if current < 0:
                current = num
            else:
                current += num
            ans = max(ans, current)
        return ans