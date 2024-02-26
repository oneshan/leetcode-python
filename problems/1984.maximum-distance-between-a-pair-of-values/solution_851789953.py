# 1984 - Maximum Distance Between a Pair of Values
# Date: 2022-11-29
# Runtime: 2966 ms, Memory: 31.1 MB
# Submission Id: 851789953


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        p1 = p2 = 0
        len_1, len_2 = len(nums1), len(nums2)
        
        while p1 < len_1 and p2 < len_2:
            if nums1[p1] > nums2[p2]:
                p1 += 1
            else:
                ans = max(ans, p2-p1)
                p2 += 1
        return ans