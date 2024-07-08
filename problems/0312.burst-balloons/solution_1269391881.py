# 0312 - Burst Balloons
# Date: 2024-05-27
# Runtime: 4960 ms, Memory: 32.6 MB
# Submission Id: 1269391881


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def dp(left, right):
            if left > right:
                return 0

            res = 0
            for i in range(left, right + 1):
                coins = nums[left-1] * nums[i] * nums[right+1]
                remains = dp(left, i-1) + dp(i+1, right)
                res = max(res, coins + remains)
            return res

        return dp(1, len(nums)-2)