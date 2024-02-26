# 0080 - Remove Duplicates from Sorted Array II
# Date: 2024-02-06
# Runtime: 58 ms, Memory: 16.6 MB
# Submission Id: 1167679503


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if idx <= 1 or nums[idx-2] != num:
                nums[idx] = num
                idx += 1
        return idx