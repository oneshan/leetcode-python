# 1569 - Max Dot Product of Two Subsequences
# Date: 2023-10-08
# Runtime: 174 ms, Memory: 16.2 MB
# Submission Id: 1069971066


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        n1, n2 = len(nums1), len(nums2)
        prev_dp = [0] * (n2+1)
        for i in range(n1-1, -1, -1):
            dp = [0] * (n2+1)
            for j in range(n2-1, -1, -1):
                dp[j] = max(
                    prev_dp[j+1] + nums1[i] * nums2[j],
                    prev_dp[j],
                    dp[j+1],
                )
            prev_dp = dp

        return dp[0]