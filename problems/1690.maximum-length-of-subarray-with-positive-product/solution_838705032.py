# 1690 - Maximum Length of Subarray With Positive Product
# Date: 2022-11-07
# Runtime: 1036 ms, Memory: 28.1 MB
# Submission Id: 838705032


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos = neg = 0
        if nums[0] > 0:
            pos = 1
        elif nums[0] < 0:
            neg = 1
            
        ans = pos
        for i in range(1, n):
            if nums[i] == 0:
                pos = neg = 0
                continue
            if nums[i] > 0:
                pos, neg = 1 + pos, 1 + neg if neg > 0 else 0
            else:
                neg, pos = 1 + pos, 1 + neg if neg > 0 else 0
            ans = max(ans, pos)
        return ans