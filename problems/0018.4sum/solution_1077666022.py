# 0018 - 4Sum
# Date: 2023-10-18
# Runtime: 136 ms, Memory: 16.5 MB
# Submission Id: 1077666022


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        def k_sum(target, k, start_idx):
            ans, avg = [], target // k
            if avg < nums[0] or avg > nums[-1]:
                return ans
            if k == 2:
                return two_sum(target, start_idx)
            
            for i in range(start_idx, n):
                if i > start_idx and nums[i] == nums[i-1]:
                    continue
                for subset in k_sum(target-nums[i], k-1, i+1):
                    ans.append([nums[i]] + subset)
            return ans
        
        def two_sum(target, start_idx):
            res = []
            left, right = start_idx, n-1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
            return res
        
        n = len(nums)
        nums.sort()
        return k_sum(target, 4, 0)