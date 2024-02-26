# 2720 - Minimize the Maximum Difference of Pairs
# Date: 2023-08-09
# Runtime: 946 ms, Memory: 30.9 MB
# Submission Id: 1016288051


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        
        def count(threshold):
            idx = count = 0
            while idx < n -1:
                if nums[idx+1] - nums[idx] <= threshold:
                    count += 1
                    idx += 1
                idx += 1
            return count
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left