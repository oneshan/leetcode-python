# 0300 - Longest Increasing Subsequence
# Date: 2023-09-21
# Runtime: 2466 ms, Memory: 18.4 MB
# Submission Id: 1055523532


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dp(i):
            ans = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans, 1 + dp(j))
            return ans
        
        return max(dp(i) for i in range(n))