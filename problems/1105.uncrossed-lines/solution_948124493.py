# 1105 - Uncrossed Lines
# Date: 2023-05-11
# Runtime: 168 ms, Memory: 16.3 MB
# Submission Id: 948124493


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        dp1 = [0] * (n2+1)
        dp2 = [0] * (n2+1)

        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp2[j+1] = dp1[j] + 1
                else:
                    dp2[j+1] = max(dp2[j], dp1[j+1])
            dp1 = dp2[:]
        return dp2[-1]