# 0219 - Contains Duplicate II
# Date: 2022-10-15
# Runtime: 1370 ms, Memory: 27.2 MB
# Submission Id: 822440146


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for idx, num in enumerate(nums):
            if num in table and idx-table[num] <= k:
                return True
            table[num] = idx
        return False