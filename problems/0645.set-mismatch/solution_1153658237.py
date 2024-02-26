# 0645 - Set Mismatch
# Date: 2024-01-22
# Runtime: 178 ms, Memory: 17.9 MB
# Submission Id: 1153658237


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # value = missing ^ dup
        dup = value = 0
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                dup = abs(nums[i])
            nums[idx] *= - 1
            value ^= (i+1) ^ abs(nums[i])
        

        return [dup, dup ^ value]