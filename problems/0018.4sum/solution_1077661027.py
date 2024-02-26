# 0018 - 4Sum
# Date: 2023-10-18
# Runtime: 483 ms, Memory: 16.4 MB
# Submission Id: 1077661027


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        n = len(nums)
        nums.sort()
        ans = []
        
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
        
        for a in range(n - 3):
            if a and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                for c, d in two_sum(target - nums[a] - nums[b], b+1):
                    ans.append([nums[a], nums[b], c, d])
        

        
        return ans