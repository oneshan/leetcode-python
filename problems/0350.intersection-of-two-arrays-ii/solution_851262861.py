# 0350 - Intersection of Two Arrays II
# Date: 2022-11-29
# Runtime: 45 ms, Memory: 14 MB
# Submission Id: 851262861


from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        table = Counter(nums1)
        ans = []
        for num in nums2:
            if table[num]:
                table[num] -= 1
                ans.append(num)
        return ans