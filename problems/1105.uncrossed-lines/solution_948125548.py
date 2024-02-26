# 1105 - Uncrossed Lines
# Date: 2023-05-11
# Runtime: 315 ms, Memory: 60.6 MB
# Submission Id: 948125548


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        @cache
        def dp(i, j):
            if i == n1 or j == n2:
                return 0
            if nums1[i] == nums2[j]:
                return 1 + dp(i+1, j+1)
            return max(dp(i+1, j), dp(i, j+1))
        
        return dp(0, 0)