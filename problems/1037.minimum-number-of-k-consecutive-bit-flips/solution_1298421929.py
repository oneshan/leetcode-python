# 1037 - Minimum Number of K Consecutive Bit Flips
# Date: 2024-06-24
# Runtime: 772 ms, Memory: 19.6 MB
# Submission Id: 1298421929


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # curr: the number of flips in nums[i-k+1:i]
        curr = ans = 0
        for i in range(n):
            if i >= k and nums[i-k] == 2:
                curr -= 1

            if curr & 1 == nums[i]:
                if i + k > n:
                    return -1
                nums[i] = 2
                curr += 1
                ans += 1

        return ans