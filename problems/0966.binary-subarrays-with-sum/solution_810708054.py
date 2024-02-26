# 0966 - Binary Subarrays With Sum
# Date: 2022-09-29
# Runtime: 628 ms, Memory: 14.9 MB
# Submission Id: 810708054


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        ans = left = count = curr_sum = 0
        for right, num in enumerate(nums):
            curr_sum += num
            if num == 1:
                count = 0
            while left <= right and curr_sum >= goal:
                if curr_sum == goal:
                    count += 1
                curr_sum -= nums[left]
                left += 1

            ans += count
                
        return ans
