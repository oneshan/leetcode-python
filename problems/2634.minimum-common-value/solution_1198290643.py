# 2634 - Minimum Common Value
# Date: 2024-03-09
# Runtime: 334 ms, Memory: 35.6 MB
# Submission Id: 1198290643


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = p2 = 0
        l1, l2 = len(nums1), len(nums2)
        while p1 < l1 and p2 < l2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                return nums1[p1]
        return -1