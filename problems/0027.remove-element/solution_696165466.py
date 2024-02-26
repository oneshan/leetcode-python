# 0027 - Remove Element
# Date: 2022-05-09
# Runtime: 61 ms, Memory: 14 MB
# Submission Id: 696165466


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == val:
                nums[i] = nums[j-1]
                j -= 1
            else:
                i += 1
        return j