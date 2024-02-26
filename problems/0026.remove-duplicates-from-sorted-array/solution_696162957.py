# 0026 - Remove Duplicates from Sorted Array
# Date: 2022-05-09
# Runtime: 93 ms, Memory: 15.7 MB
# Submission Id: 696162957


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if not idx or num != nums[idx-1]:
                nums[idx] = num
                idx += 1
        return idx