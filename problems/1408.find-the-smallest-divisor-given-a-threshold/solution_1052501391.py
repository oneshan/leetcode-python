# 1408 - Find the Smallest Divisor Given a Threshold
# Date: 2023-09-18
# Runtime: 394 ms, Memory: 22.4 MB
# Submission Id: 1052501391


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def is_valid(divisor):
            total = 0
            for num in nums:
                total += math.ceil(num / divisor)
                if total > threshold:
                    return False
            return True
        
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        return left