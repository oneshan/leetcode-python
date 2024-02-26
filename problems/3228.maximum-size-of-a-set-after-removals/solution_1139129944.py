# 3228 - Maximum Size of a Set After Removals
# Date: 2024-01-07
# Runtime: 615 ms, Memory: 26.5 MB
# Submission Id: 1139129944


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1) // 2, len(nums2) // 2
        
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        for num in c1:
            n1 -= c1[num]-1
        for num in c2:
            n2 -= c2[num]-1
        
        ans = len(set(c1 + c2))
        inter = len(c1 & c2)

        if n1 > 0:
            if inter > n1:
                inter -= n1
            else:
                ans -= (n1-inter)
                inter = 0

        if n2 > 0:
            if inter > n2:
                inter -= n2
            else:
                ans -= (n2-inter)
                inter = 0

        return ans