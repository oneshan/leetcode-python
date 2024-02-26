# 0027 - Remove Element
# Date: 2023-07-22
# Runtime: 54 ms, Memory: 16.3 MB
# Submission Id: 1000663594


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for num in nums:
            if num != val:
                nums[idx] = num
                idx += 1
        return idx