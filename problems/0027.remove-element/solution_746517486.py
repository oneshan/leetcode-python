# 0027 - Remove Element
# Date: 2022-07-14
# Runtime: 53 ms, Memory: 13.8 MB
# Submission Id: 746517486


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for num in nums:
            if num != val:
                nums[idx] = num
                idx += 1
        return idx