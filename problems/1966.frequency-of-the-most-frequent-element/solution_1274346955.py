# 1966 - Frequency of the Most Frequent Element
# Date: 2024-06-02
# Runtime: 1036 ms, Memory: 30.4 MB
# Submission Id: 1274346955


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = curr = left = 0
        for right, num in enumerate(nums):
            curr += num
            while num * (right-left+1) - curr > k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right-left+1)
        return ans