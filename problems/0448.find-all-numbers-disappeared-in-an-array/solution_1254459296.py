# 0448 - Find All Numbers Disappeared in an Array
# Date: 2024-05-10
# Runtime: 266 ms, Memory: 24.8 MB
# Submission Id: 1254459296


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i])-1
            if idx < n and nums[idx] > 0:
                nums[idx] *= -1

        return [i+1 for i in range(n) if nums[i] > 0]