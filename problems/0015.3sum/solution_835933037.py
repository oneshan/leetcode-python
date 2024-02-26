# 0015 - 3Sum
# Date: 2022-11-03
# Runtime: 3303 ms, Memory: 18.2 MB
# Submission Id: 835933037


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(n-2):
            if i and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: j += 1
                    while j < k and nums[k] == nums[k+1]: k -= 1 
                elif three_sum > 0:
                    k -= 1
                else:
                    j += 1
        return ans