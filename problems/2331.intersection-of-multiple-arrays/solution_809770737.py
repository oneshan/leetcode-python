# 2331 - Intersection of Multiple Arrays
# Date: 2022-09-27
# Runtime: 156 ms, Memory: 14.4 MB
# Submission Id: 809770737


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for arr in nums:
            ans &= set(arr)
        
        return [num for num in range(1, 1001) if num in ans]