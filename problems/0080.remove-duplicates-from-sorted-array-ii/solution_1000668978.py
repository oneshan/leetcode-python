# 0080 - Remove Duplicates from Sorted Array II
# Date: 2023-07-22
# Runtime: 73 ms, Memory: 16.3 MB
# Submission Id: 1000668978


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if idx <= 1 or nums[idx-2] != num:
                nums[idx] = num
                idx += 1
        return idx