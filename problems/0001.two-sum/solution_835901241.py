# 0001 - Two Sum
# Date: 2022-11-03
# Runtime: 69 ms, Memory: 15.5 MB
# Submission Id: 835901241


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, num in enumerate(nums):
            if num in table:
                return [table[num], idx]
            table[target-num] = idx