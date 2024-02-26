# 1690 - Maximum Length of Subarray With Positive Product
# Date: 2022-11-07
# Runtime: 1636 ms, Memory: 28.1 MB
# Submission Id: 838705832


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for num in nums:
            if num == 0:
                pos = neg = 0
            elif num > 0:
                pos, neg = 1 + pos, 1 + neg if neg > 0 else 0
            else:
                neg, pos = 1 + pos, 1 + neg if neg > 0 else 0
            ans = max(ans, pos)
        return ans