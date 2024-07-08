# 1046 - Max Consecutive Ones III
# Date: 2024-06-05
# Runtime: 453 ms, Memory: 17 MB
# Submission Id: 1278259426


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = left = 0
        for right in range(n):
            k -= (1 - nums[right])
            if k < 0:
                k += (1 - nums[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans