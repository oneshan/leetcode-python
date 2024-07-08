# 1046 - Max Consecutive Ones III
# Date: 2024-06-05
# Runtime: 469 ms, Memory: 17 MB
# Submission Id: 1278258592


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = left = count = 0
        for right in range(n):
            count += nums[right]
            while (right - left + 1) - count > k:
                count -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans