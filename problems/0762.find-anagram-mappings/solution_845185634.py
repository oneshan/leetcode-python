# 0762 - Find Anagram Mappings
# Date: 2022-11-17
# Runtime: 41 ms, Memory: 14 MB
# Submission Id: 845185634


from collections import defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = defaultdict(list)
        for idx, num in enumerate(nums2):
            table[num].append(idx)
        
        return [table[num].pop() for idx, num in enumerate(nums1)]