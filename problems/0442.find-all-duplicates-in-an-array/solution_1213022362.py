# 0442 - Find All Duplicates in an Array
# Date: 2024-03-25
# Runtime: 280 ms, Memory: 23.6 MB
# Submission Id: 1213022362


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums += [0]
        nums[0], nums[-1] = nums[-1], nums[0]

        for i in range(1, len(nums)):
            j = nums[i]
            while nums[i] != i and nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i]

        return [nums[i] for i in range(1, len(nums)) if nums[i] != i]