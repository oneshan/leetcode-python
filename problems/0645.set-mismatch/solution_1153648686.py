# 0645 - Set Mismatch
# Date: 2024-01-22
# Runtime: 186 ms, Memory: 17.9 MB
# Submission Id: 1153648686


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup, missing = -1, 1
        for i in range(n):
            if nums[abs(nums[i])-1] < 0:
                dup = abs(nums[i])
            else:
                nums[abs(nums[i])-1] *= -1
        
        for i in range(1, n):
            if nums[i] > 0:
                missing = i+1
        
        return [dup, missing]