# 0219 - Contains Duplicate II
# Date: 2022-07-17
# Runtime: 631 ms, Memory: 27.2 MB
# Submission Id: 748901784


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for idx, num in enumerate(nums):
            if num in last_seen:
                last_idx = last_seen[num]
                if idx - last_idx <= k:
                    return True
            last_seen[num] = idx
        return False