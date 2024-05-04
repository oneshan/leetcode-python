# 0718 - Maximum Length of Repeated Subarray
# Date: 2024-05-03
# Runtime: 1569 ms, Memory: 16.7 MB
# Submission Id: 1248059788


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        
        dp = [0] * (len2 + 1)
        ans = 0
        for p1 in range(len1):
            next_dp = [0] * (len2 + 1)
            for p2 in range(len2):
                if nums1[p1] == nums2[p2]:
                    next_dp[p2+1] = 1 + dp[p2]
                ans = max(ans, next_dp[p2+1])
            dp = next_dp
        return ans