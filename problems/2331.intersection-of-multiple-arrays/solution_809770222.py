# 2331 - Intersection of Multiple Arrays
# Date: 2022-09-27
# Runtime: 123 ms, Memory: 14.3 MB
# Submission Id: 809770222


from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for arr in nums:
            ans &= set(arr)
        
        return sorted(list(ans))