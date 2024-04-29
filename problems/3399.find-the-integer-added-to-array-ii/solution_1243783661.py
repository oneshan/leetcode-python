# 3399 - Find the Integer Added to Array II
# Date: 2024-04-28
# Runtime: 47 ms, Memory: 16.5 MB
# Submission Id: 1243783661


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        nums1.sort()
        nums2.sort()
        
        diffs = [nums2[0] - nums1[0], nums2[0] - nums1[1], nums2[0] - nums1[2]]
        
        for diff in sorted(diffs):
            i = j = count = 0
            while j < n-2:
                if nums1[i] + diff == nums2[j]:
                    i += 1
                    j += 1
                else:
                    count += 1
                    i += 1
                if count > 2:
                    break
            if count < 3:
                return diff
        return -1