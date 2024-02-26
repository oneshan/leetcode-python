# 0410 - Split Array Largest Sum
# Date: 2023-09-18
# Runtime: 50 ms, Memory: 16.4 MB
# Submission Id: 1052602258


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(max_sum):
            curr_sum = curr_group = 0
            for num in nums:
                if curr_sum + num <= max_sum:
                    curr_sum += num
                else:
                    curr_sum = num
                    curr_group += 1
                    if curr_group >= k:
                        return False
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left