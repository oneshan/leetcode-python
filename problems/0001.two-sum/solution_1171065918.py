# 0001 - Two Sum
# Date: 2024-02-10
# Runtime: 50 ms, Memory: 18 MB
# Submission Id: 1171065918


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, num in enumerate(nums):
            if num in table:
                return [table[num], idx]
            table[target-num] = idx