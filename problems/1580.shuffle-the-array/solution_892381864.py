# 1580 - Shuffle the Array
# Date: 2023-02-06
# Runtime: 70 ms, Memory: 14 MB
# Submission Id: 892381864


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        for i in range(n):
            nums[n+i] += nums[i] << 10
        for i in range(n):
            nums[2*i] = nums[n+i] >> 10
            nums[2*i+1] = nums[n+i] & 1023
        return nums