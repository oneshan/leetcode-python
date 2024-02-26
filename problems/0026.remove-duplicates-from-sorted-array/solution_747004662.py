# 0026 - Remove Duplicates from Sorted Array
# Date: 2022-07-14
# Runtime: 167 ms, Memory: 15.6 MB
# Submission Id: 747004662


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if not idx or num != nums[idx-1]:
                nums[idx] = num
                idx += 1
        return idx