# 0001 - Two Sum
# Date: 2022-05-03
# Runtime: 68 ms, Memory: 15.4 MB
# Submission Id: 692372917


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, num in enumerate(nums):
            if num in table:
                return [table[num], idx]
            table[target - num] = idx