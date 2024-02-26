# 1621 - Number of Subsequences That Satisfy the Given Sum Condition
# Date: 2023-05-06
# Runtime: 895 ms, Memory: 28.6 MB
# Submission Id: 945277174


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        mod = 10 ** 9 + 7
        
        ans = 0
        for left in range(n):
            right = bisect.bisect_right(nums, target - nums[left]) - 1
            if right >= left:
                ans += pow(2, right - left, mod)

        return ans % mod