# 2552 - Maximum Sum of Distinct Subarrays With Length K
# Date: 2022-11-06
# Runtime: 845 ms, Memory: 31.8 MB
# Submission Id: 837737204


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = {}
        
        ans = 0
        curr_sum = left = 0
        for idx, num in enumerate(nums):
            curr_sum += num
            
            while left <= seen.get(num, -1):
                curr_sum -= nums[left]
                left += 1
                
            while idx - left + 1 > k:
                curr_sum -= nums[left]
                left += 1
    
            seen[num] = idx
            if idx - left + 1== k:
                ans = max(ans, curr_sum)
        return ans