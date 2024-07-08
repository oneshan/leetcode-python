# 0018 - 4Sum
# Date: 2024-06-08
# Runtime: 377 ms, Memory: 16.6 MB
# Submission Id: 1281324292


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            for arr in self.threeSum(nums, target-nums[i], i+1):
                ans.append([nums[i]] + arr)
        return ans
    
    def threeSum(self, nums, target, left):
        res = []
        for i in range(left, len(nums)):
            if i > left and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif three_sum < target:
                    j += 1
                else:
                    k -= 1
        return res