# 2211 - K Radius Subarray Averages
# Date: 2023-08-15
# Runtime: 1247 ms, Memory: 34.9 MB
# Submission Id: 1022191203


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        size = 2*k + 1
        ans = [-1] * n

        if n < size:
            return ans
        
        prefix_sum = 0
        for i in range(size):
            prefix_sum += nums[i]
        
        ans[k] = prefix_sum // size
        for i in range(size, n):
            prefix_sum = prefix_sum - nums[i-size] + nums[i]
            ans[i-k] = prefix_sum // size
        return ans