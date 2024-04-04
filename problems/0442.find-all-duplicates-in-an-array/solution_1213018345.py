# 0442 - Find All Duplicates in an Array
# Date: 2024-03-25
# Runtime: 259 ms, Memory: 24.8 MB
# Submission Id: 1213018345


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            idx = abs(num)-1
            if nums[idx] < 0:
                ans.append(abs(num))
            nums[idx] *= -1
        return ans