# 0349 - Intersection of Two Arrays
# Date: 2022-09-27
# Runtime: 97 ms, Memory: 14 MB
# Submission Id: 809120567


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        ans = []
        len_1, len_2 = len(nums1), len(nums2)
        p1 = p2 = 0
        while p1 < len_1 and p2 < len_2:
            n1, n2 = nums1[p1], nums2[p2]
            if n1 == n2:
                ans.append(nums1[p1])
                while p1 < len_1 and nums1[p1] == n1: p1 += 1
                while p2 < len_2 and nums2[p2] == n2: p2 += 1
            elif n1 > n2:
                p2 += 1
            else:
                p1 += 1
        return ans