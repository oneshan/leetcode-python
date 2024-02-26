# 3154 - Maximum Value of an Ordered Triplet I
# Date: 2023-10-01
# Runtime: 230 ms, Memory: 16.3 MB
# Submission Id: 1063568605


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    ans = max(ans, (nums[i]-nums[j]) * nums[k])
        return ans