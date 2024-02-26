# 1580 - Shuffle the Array
# Date: 2022-11-18
# Runtime: 70 ms, Memory: 14.2 MB
# Submission Id: 845805710


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (2*n)
        j = 0
        for i in range(n):
            ans[j], ans[j+1] = nums[i], nums[n+i]
            j += 2
        return ans