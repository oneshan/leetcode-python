# 0045 - Jump Game II
# Date: 2023-02-08
# Runtime: 137 ms, Memory: 15 MB
# Submission Id: 893822589


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        curr_end = max_end = 0
        
        for i in range(n-1):
            max_end = max(max_end, i + nums[i])
            if i == curr_end:
                ans += 1
                curr_end = max_end
        return ans