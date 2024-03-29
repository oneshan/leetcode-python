# 0456 - 132 Pattern
# Date: 2023-09-30
# Runtime: 389 ms, Memory: 36.4 MB
# Submission Id: 1062855021


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        n = len(nums)
        min_arr = [float('inf')] * n
        min_arr[0] = nums[0]
        for i in range(1, n):
            min_arr[i] = min(min_arr[i-1], nums[i])
        
        
        stack = []
        for j in range(n-1, -1, -1):
            if nums[j] <= min_arr[j]:
                continue
            while stack and stack[-1] <= min_arr[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False