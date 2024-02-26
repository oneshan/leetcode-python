# 0349 - Intersection of Two Arrays
# Date: 2022-07-16
# Runtime: 63 ms, Memory: 14.2 MB
# Submission Id: 748355572


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table, ans = set(), set()
        for num in nums1:
            table.add(num)
        for num in nums2:
            if num in table:
                ans.add(num)
        return list(ans)