# 0446 - Arithmetic Slices II - Subsequence
# Date: 2024-06-19
# Runtime: 598 ms, Memory: 71.1 MB
# Submission Id: 1292845533


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]

        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = dp[j][diff]
                dp[i][diff] += 1 + cnt
                ans += cnt 
        return ans