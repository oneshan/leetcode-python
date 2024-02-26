# 0349 - Intersection of Two Arrays
# Date: 2022-07-16
# Runtime: 62 ms, Memory: 14 MB
# Submission Id: 748360852


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        ans = []
        p1 = p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            n1, n2 = nums1[p1], nums2[p2]
            if n1 == n2:
                ans.append(n1)
                while p1 < len(nums1) and nums1[p1] == n1: p1+=1
                while p2 < len(nums2) and nums2[p2] == n2: p2+=1
            elif n1 > n2:
                while p2 < len(nums2) and nums2[p2] == n2: p2+=1
            else:
                while p1 < len(nums1) and nums1[p1] == n1: p1+=1
        return ans