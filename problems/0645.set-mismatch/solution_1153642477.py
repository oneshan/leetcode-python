# 0645 - Set Mismatch
# Date: 2024-01-22
# Runtime: 162 ms, Memory: 18.7 MB
# Submission Id: 1153642477


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        table = set()
        value = dup_num = 0
        for idx, num in enumerate(nums, 1):
            value ^= idx ^ num
            if num in table:
                dup_num = num
            table.add(num)
        return [dup_num, dup_num ^ value]
