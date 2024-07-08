# 0045 - Jump Game II
# Date: 2024-05-23
# Runtime: 103 ms, Memory: 17.5 MB
# Submission Id: 1265386730


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = curr_max = temp = 0
        for i in range(n):
            if i > curr_max:
                curr_max = temp
                ans += 1
            temp = max(temp, i+nums[i])

        return ans