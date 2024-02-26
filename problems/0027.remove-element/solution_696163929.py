# 0027 - Remove Element
# Date: 2022-05-09
# Runtime: 62 ms, Memory: 14 MB
# Submission Id: 696163929


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for num in nums:
            if num == val:
                continue
            nums[idx] = num
            idx += 1
        return idx