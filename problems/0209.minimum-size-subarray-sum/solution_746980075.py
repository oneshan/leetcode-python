# 0209 - Minimum Size Subarray Sum
# Date: 2022-07-14
# Runtime: 530 ms, Memory: 27.3 MB
# Submission Id: 746980075


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = left = 0
        ans = 100001
        for idx, num in enumerate(nums):
            curr += num
            while curr >= target:
                ans = min(ans, 1+idx-left)
                curr -= nums[left]
                left += 1
        return 0 if ans == 100001 else ans