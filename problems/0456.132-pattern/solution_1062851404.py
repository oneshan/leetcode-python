# 0456 - 132 Pattern
# Date: 2023-09-30
# Runtime: 418 ms, Memory: 36.3 MB
# Submission Id: 1062851404


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        n = len(nums)
        min_arr = [float('inf')] * n
        min_arr[0] = nums[0]
        for i in range(1, n):
            min_arr[i] = min(min_arr[i-1], nums[i])
        
        k = n
        for j in range(n-1, -1, -1):
            if nums[j] <= min_arr[j]:
                continue
            while k < n and nums[k] <= min_arr[j]:
                k += 1
            if k < n and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
        return False