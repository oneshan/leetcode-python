# 0004 - Median of Two Sorted Arrays
# Date: 2023-09-21
# Runtime: 93 ms, Memory: 16.3 MB
# Submission Id: 1055515839


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        left, right = 0, len1
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = (len1 + len2 + 1) // 2 - mid1
            
            left1 = float('-inf') if mid1 == 0 else nums1[mid1-1]
            right1 = float('inf') if mid1 == len1 else nums1[mid1]
            left2 = float('-inf') if mid2 == 0 else nums2[mid2-1]
            right2 = float('inf') if mid2 == len2 else nums2[mid2]
            
            if left1 <= right2 and left2 <= right1:
                if (len1 + len2) & 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2
            
            if left1 > right2:
                right = mid1 - 1
            else:
                left = mid1 + 1