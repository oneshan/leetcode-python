# 0446 - Arithmetic Slices II - Subsequence
# Date: 2024-01-07
# Runtime: 1001 ms, Memory: 188.6 MB
# Submission Id: 1139318474


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = defaultdict(int)
        
        for right in range(1, n):
            for left in range(right):
                diff = nums[right] - nums[left]
                dp[(right, diff)] += dp[(left, diff)] + 1
                ans += dp[(left, diff)]
        return ans