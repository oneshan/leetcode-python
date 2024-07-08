# 0350 - Intersection of Two Arrays II
# Date: 2024-07-02
# Runtime: 41 ms, Memory: 16.8 MB
# Submission Id: 1306420145


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        ans = []
        for num in nums2:
            if counter[num]:
                ans.append(num)
                counter[num] -= 1
        return ans