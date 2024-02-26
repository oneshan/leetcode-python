# 0209 - Minimum Size Subarray Sum
# Date: 2023-08-17
# Runtime: 205 ms, Memory: 29.6 MB
# Submission Id: 1023781605


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1
        curr = left = 0        
        for right in range(n):
            curr += nums[right]
            if curr >= target:
                while curr - nums[left] >= target:
                    curr -= nums[left]
                    left += 1
                ans = min(ans, right-left+1)
        return ans if ans != n+1 else 0