# 0219 - Contains Duplicate II
# Date: 2022-07-17
# Runtime: 724 ms, Memory: 27.2 MB
# Submission Id: 748903502


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for idx, num in enumerate(nums):
            if table.get(num, 0):
                return True
            table[num] = table.get(num, 0) + 1
            if idx >= k:
                table[nums[idx-k]] -= 1
        return False