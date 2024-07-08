# 0220 - Contains Duplicate III
# Date: 2024-06-20
# Runtime: 764 ms, Memory: 34.2 MB
# Submission Id: 1294559857


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        size = valueDiff + 1

        buckets = {}

        for idx, num in enumerate(nums):
            bucket_idx = num // size

            if bucket_idx in buckets:
                return True

            if bucket_idx - 1 in buckets and num - buckets[bucket_idx-1] <= valueDiff:
                return True

            if bucket_idx + 1 in buckets and buckets[bucket_idx+1] - num <= valueDiff:
                return True

            buckets[bucket_idx] = num
            if idx >= indexDiff:
                buckets.pop(nums[idx-indexDiff] // size)

        return False