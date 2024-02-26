# 1690 - Maximum Length of Subarray With Positive Product
# Date: 2022-11-07
# Runtime: 1712 ms, Memory: 28.1 MB
# Submission Id: 838700141


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        left, neg_count, ans = 0, 0, 0
        
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                neg_count += 1
            if nums[i] == 0 or i == n-1:
                j, k = left, i
                if nums[i] == 0:
                    k -= 1
                if neg_count & 1 == 0:
                    ans = max(ans, k-j+1)
                else:
                    while j < k and nums[j] >= 0: j += 1
                    while j < k and nums[k] >= 0: k -= 1
                    ans = max(ans, k-left, i-j-(nums[i]==0))
                left, neg_count = i+1, 0
        
        return ans