# 0219 - Contains Duplicate II
# Date: 2024-02-10
# Runtime: 454 ms, Memory: 29.9 MB
# Submission Id: 1171066872


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for idx, num in enumerate(nums):
            if num in table and idx - table[num] <= k:
                return True
            table[num] = idx
        return False