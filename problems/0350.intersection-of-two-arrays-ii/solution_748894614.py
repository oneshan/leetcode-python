# 0350 - Intersection of Two Arrays II
# Date: 2022-07-17
# Runtime: 60 ms, Memory: 14.1 MB
# Submission Id: 748894614


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        ans = []
        for num in nums2:
            if table.get(num, 0):
                ans.append(num)
                table[num] -= 1
        return ans