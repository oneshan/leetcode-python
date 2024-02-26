# 0041 - First Missing Positive
# Date: 2022-10-18
# Runtime: 785 ms, Memory: 27.1 MB
# Submission Id: 824576178


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        has_one = False
        for i in range(n):
            if nums[i] == 1:
                has_one = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        if not has_one:
            return 1
        
        for i in range(n):
            idx = abs(nums[i])
            if idx == n:
                nums[0] = -abs(nums[0])
            else:
                nums[idx] = -abs(nums[idx])
        
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
        return n + 1