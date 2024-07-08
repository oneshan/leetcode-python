# 0416 - Partition Equal Subset Sum
# Date: 2024-05-25
# Runtime: 158 ms, Memory: 19.2 MB
# Submission Id: 1266789190


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1:
            return False

        target = total >> 1
        subset = {0}
        for num in nums:
            added = {prev + num for prev in subset}
            subset |= added
            if target in subset:
                return True
        return False