# 0026 - Remove Duplicates from Sorted Array
# Date: 2023-07-22
# Runtime: 97 ms, Memory: 18 MB
# Submission Id: 1000664539


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if num != nums[idx]:
                idx += 1
                nums[idx] = num
        return idx + 1