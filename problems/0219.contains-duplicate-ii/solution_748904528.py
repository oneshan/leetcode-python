# 0219 - Contains Duplicate II
# Date: 2022-07-17
# Runtime: 951 ms, Memory: 25.4 MB
# Submission Id: 748904528


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for idx, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if idx >= k:
                seen.remove(nums[idx-k])
        return False