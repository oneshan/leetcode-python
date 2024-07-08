# 0446 - Arithmetic Slices II - Subsequence
# Date: 2024-06-19
# Runtime: 875 ms, Memory: 71.1 MB
# Submission Id: 1292844994


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [defaultdict(int) for _ in range(n)]

        ans = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                ans += dp[j][diff]

        return ans