# 0018 - 4Sum
# Date: 2024-06-08
# Runtime: 337 ms, Memory: 16.5 MB
# Submission Id: 1281334936


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 0, 4)

    def kSum(self, nums, target, left, k):
        res = []
            
        if k == 2:
            return self.twoSum(nums, target, left)
        
        for i in range(left, len(nums)):
            if i > left and nums[i] == nums[i-1]:
                continue
            for subset in self.kSum(nums, target-nums[i], i+1, k-1):
                res.append([nums[i]] + subset)

        return res
    
    def twoSum(self, nums, target, left):
        res = []
        right = len(nums)-1
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                res.append([nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1
        return res