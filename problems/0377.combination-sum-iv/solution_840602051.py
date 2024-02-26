# 0377 - Combination Sum IV
# Date: 2022-11-10
# Runtime: 89 ms, Memory: 14 MB
# Submission Id: 840602051


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]