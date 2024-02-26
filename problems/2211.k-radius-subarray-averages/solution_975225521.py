# 2211 - K Radius Subarray Averages
# Date: 2023-06-20
# Runtime: 1650 ms, Memory: 35.2 MB
# Submission Id: 975225521


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        ans = [-1] * n
        if n < 2*k+1:
            return ans
        
        win_sum = 0
        for i in range(n):
            win_sum += nums[i]
            if i >= 2 * k:
                ans[i-k] = win_sum // (2*k+1)
                win_sum -= nums[i- 2*k]
        return ans