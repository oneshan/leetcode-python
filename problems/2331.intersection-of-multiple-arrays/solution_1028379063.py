# 2331 - Intersection of Multiple Arrays
# Date: 2023-08-22
# Runtime: 72 ms, Memory: 16.8 MB
# Submission Id: 1028379063


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for arr in nums:
            ans &= set(arr)
        return sorted(ans)