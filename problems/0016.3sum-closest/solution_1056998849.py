# 0016 - 3Sum Closest
# Date: 2023-09-23
# Runtime: 641 ms, Memory: 16.3 MB
# Submission Id: 1056998849


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        for i in range(n):
            j, k = i+1, n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(target - total) < abs(diff):
                    diff = target - total
                if total == target:
                    return target
                if total < target:
                    j += 1
                else:
                    k -= 1
        return target - diff