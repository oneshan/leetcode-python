# 1580 - Shuffle the Array
# Date: 2023-02-06
# Runtime: 55 ms, Memory: 14.2 MB
# Submission Id: 892381001


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (n*2)
        for i in range(n):
            ans[2*i] = nums[i]
            ans[2*i+1] = nums[i+n]
        return ans