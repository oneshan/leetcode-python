# 1580 - Shuffle the Array
# Date: 2022-11-19
# Runtime: 149 ms, Memory: 14.1 MB
# Submission Id: 846206802


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        for i in range(n):
            nums[n+i] = nums[n+i] << 10 | nums[i]
            
        for i in range(n):
            nums[2*i] = nums[n+i] & 1023
            nums[2*i+1] = nums[n+i] >> 10
        return nums