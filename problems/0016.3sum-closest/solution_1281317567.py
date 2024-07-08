# 0016 - 3Sum Closest
# Date: 2024-06-08
# Runtime: 355 ms, Memory: 16.6 MB
# Submission Id: 1281317567


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        ans = min_diff = float('inf')
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == target:
                    return target
                if abs(three_sum - target) < min_diff:
                    min_diff, ans = abs(three_sum - target), three_sum
                if three_sum < target:
                    j += 1
                else:
                    k -= 1        
        return ans