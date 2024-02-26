# 0209 - Minimum Size Subarray Sum
# Date: 2022-07-14
# Runtime: 647 ms, Memory: 27.4 MB
# Submission Id: 747002100


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # prefix sum
        prefix_sum = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        
        ans = 100001
        for i in range(len(prefix_sum)):
            val = target + prefix_sum[i]
            
            left, right = i+1, len(prefix_sum)-1
            while left <= right:
                mid = (left + right) // 2
                if prefix_sum[mid] < val:
                    left = mid +1
                else:
                    right = mid -1
            
            if left == len(prefix_sum):
                break
            ans = min(ans, left - i)
    
        return ans if ans < 100001 else 0