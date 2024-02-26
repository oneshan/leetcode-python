# 0053 - Maximum Subarray
# Date: 2022-10-25
# Runtime: 5941 ms, Memory: 41.9 MB
# Submission Id: 829908765


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def recur(left, right):
            if left > right:
                return float('-inf')
            
            mid = (left + right) // 2
            left_sum = right_sum = 0
            
            curr = 0
            for i in range(mid-1, left-1, -1):
                curr += nums[i]
                left_sum = max(left_sum, curr)
            
            curr = 0
            for i in range(mid+1, right+1):
                curr += nums[i]
                right_sum = max(right_sum, curr)
                
            return max(nums[mid] + left_sum + right_sum,
                       recur(left, mid-1),
                       recur(mid+1, right))
        
        return recur(0, len(nums)-1)