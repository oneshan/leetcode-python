# 0026 - Remove Duplicates from Sorted Array
# Date: 2022-09-15
# Runtime: 200 ms, Memory: 15.5 MB
# Submission Id: 800421997


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if num != nums[idx]:
                idx += 1
                nums[idx] = num
        return idx + 1