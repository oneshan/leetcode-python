# 0209 - Minimum Size Subarray Sum
# Date: 2024-05-31
# Runtime: 315 ms, Memory: 30.1 MB
# Submission Id: 1273178417


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        def is_valid(k):
            total = 0
            for i in range(len(nums)):
                total += nums[i]
                if i >= k:
                    total -= nums[i-k]
                if total >= target:
                    return True
            return False

        left, right = 1, len(nums) + 1
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if left < len(nums) + 1 else 0