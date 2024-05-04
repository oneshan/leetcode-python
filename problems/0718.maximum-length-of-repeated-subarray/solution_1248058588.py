# 0718 - Maximum Length of Repeated Subarray
# Date: 2024-05-03
# Runtime: 2049 ms, Memory: 41.5 MB
# Submission Id: 1248058588


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        
        dp = [[0] * (len2+1) for _ in range(len1+1)]
        ans = 0
        for p1 in range(len1):
            for p2 in range(len2):
                if nums1[p1] == nums2[p2]:
                    dp[p1+1][p2+1] = 1 + dp[p1][p2]
                else:
                    dp[p1+1][p2+1] = 0
                ans = max(ans, dp[p1+1][p2+1])
        return ans