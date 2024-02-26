# 1621 - Number of Subsequences That Satisfy the Given Sum Condition
# Date: 2023-05-06
# Runtime: 804 ms, Memory: 28.6 MB
# Submission Id: 945276297


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        mod = 10 ** 9 + 7
        
        left, right = 0, n-1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + pow(2, right-left, mod)) % mod
                left += 1
            else:
                right -= 1
        return ans