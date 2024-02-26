# 0004 - Median of Two Sorted Arrays
# Date: 2023-09-21
# Runtime: 79 ms, Memory: 16.6 MB
# Submission Id: 1055459210


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        
        p1 = p2 = 0
        def get_min():
            nonlocal p1, p2
            result = 0
            if p1 == len1:
                result = nums2[p2]
                p2 += 1
            elif p2 == len2:
                result = nums1[p1]
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                result = nums1[p1]
                p1 += 1
            else:
                result = nums2[p2]
                p2 += 1
            return result
                    
        if (len1 + len2) & 1:
            for _ in range((len1+len2) // 2):
                get_min()
            return get_min()
        
        for _ in range((len1+len2) // 2 - 1):
            get_min()
        return (get_min() + get_min()) / 2

    