# 0762 - Find Anagram Mappings
# Date: 2022-11-17
# Runtime: 31 ms, Memory: 13.8 MB
# Submission Id: 845186068


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        for idx, num in enumerate(nums2):
            table[num] = idx
        
        return [table[num] for num in nums1]