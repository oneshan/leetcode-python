# 0004 - Median of Two Sorted Arrays
# Date: 2023-09-21
# Runtime: 94 ms, Memory: 16.6 MB
# Submission Id: 1055495542


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        
        prev = curr = 0
        p1 = p2 = 0
        
        for _ in range((len1 + len2) // 2 + 1):
            prev = curr
            if p1 == len1:
                curr = nums2[p2]
                p2 += 1
            elif p2 == len2:
                curr = nums1[p1]
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                curr = nums1[p1]
                p1 += 1
            else:
                curr = nums2[p2]
                p2 += 1
                
        if (len1 + len2) & 1:
            return curr
        return (prev + curr) / 2
    