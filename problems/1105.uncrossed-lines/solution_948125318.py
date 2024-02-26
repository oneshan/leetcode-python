# 1105 - Uncrossed Lines
# Date: 2023-05-11
# Runtime: 360 ms, Memory: 60.6 MB
# Submission Id: 948125318


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        @cache
        def dp(i, j):
            if i <= 0 or j <= 0:
                return 0
            if nums1[i-1] == nums2[j-1]:
                return 1 + dp(i-1, j-1)
            return max(dp(i-1, j), dp(i, j-1))
        
        return dp(n1, n2)