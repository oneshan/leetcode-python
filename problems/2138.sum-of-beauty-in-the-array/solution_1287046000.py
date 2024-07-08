# 2138 - Sum of Beauty in the Array
# Date: 2024-06-13
# Runtime: 798 ms, Memory: 30.4 MB
# Submission Id: 1287046000


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        curr_max, curr_min = float('-inf'), float('inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            curr_min = min(curr_min, nums[~i])
            prefix[i] = curr_max
            suffix[~i] = curr_min

        ans = 0
        for i in range(1, n-1):
            if prefix[i-1] < nums[i] < suffix[i+1]:
                ans += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                ans += 1
        return ans