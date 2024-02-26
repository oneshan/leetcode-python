# 0169 - Majority Element
# Date: 2024-02-06
# Runtime: 135 ms, Memory: 18 MB
# Submission Id: 1167680418


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        count = 0
        for num in nums:
            if ans == num:
                count += 1
            else:
                count -= 1
            if count < 0:
                ans, count = num, 1
        return ans