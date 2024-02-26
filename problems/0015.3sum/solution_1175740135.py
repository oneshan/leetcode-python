# 0015 - 3Sum
# Date: 2024-02-15
# Runtime: 599 ms, Memory: 20.8 MB
# Submission Id: 1175740135


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = []
        for i in range(n-2):
            if i and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            target = -nums[i]
            while j < k:
                total = nums[j] + nums[k]
                if total == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif total < target:
                    j += 1
                else:
                    k -= 1
        return ans