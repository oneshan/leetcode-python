# 0026 - Remove Duplicates from Sorted Array
# Date: 2024-02-06
# Runtime: 62 ms, Memory: 17.9 MB
# Submission Id: 1167677786


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if nums[idx] != num:
                idx += 1
                nums[idx] = num
        return idx + 1