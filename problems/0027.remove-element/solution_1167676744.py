# 0027 - Remove Element
# Date: 2024-02-06
# Runtime: 36 ms, Memory: 16.6 MB
# Submission Id: 1167676744


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for num in nums:
            if num != val:
                nums[idx] = num
                idx += 1
        return idx