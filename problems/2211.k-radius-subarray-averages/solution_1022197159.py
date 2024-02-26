# 2211 - K Radius Subarray Averages
# Date: 2023-08-15
# Runtime: 1248 ms, Memory: 35.1 MB
# Submission Id: 1022197159


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        size = 2*k + 1
        ans = [-1] * n

        if n < size:
            return ans
        
        window_sum = 0
        for i in range(n):
            window_sum += nums[i]
            if i >= size-1:
                ans[i-k] = window_sum // size
                window_sum -= nums[i+1-size]

        return ans