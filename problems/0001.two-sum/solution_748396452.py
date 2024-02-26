# 0001 - Two Sum
# Date: 2022-07-16
# Runtime: 117 ms, Memory: 15.4 MB
# Submission Id: 748396452


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, num in enumerate(nums):
            if num in table:
                return [table[num], idx]
            table[target-num] = idx