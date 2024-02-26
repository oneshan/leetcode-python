# 1083 - Two Sum Less Than K
# Date: 2023-10-29
# Runtime: 39 ms, Memory: 16.1 MB
# Submission Id: 1086779455


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        ans = -1
        left, right = 0, n - 1
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum < k:
                ans = max(ans, two_sum)
                left += 1
            else:
                right -= 1
        return ans