# 1569 - Max Dot Product of Two Subsequences
# Date: 2023-10-08
# Runtime: 211 ms, Memory: 19 MB
# Submission Id: 1069969121


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                dp[i][j] = max(
                    dp[i+1][j+1] + nums1[i] * nums2[j],
                    dp[i+1][j],
                    dp[i][j+1]

                )

        return dp[0][0]