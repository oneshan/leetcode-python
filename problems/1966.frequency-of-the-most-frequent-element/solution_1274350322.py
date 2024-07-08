# 1966 - Frequency of the Most Frequent Element
# Date: 2024-06-02
# Runtime: 880 ms, Memory: 30.4 MB
# Submission Id: 1274350322


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = curr = left = 0
        for right, num in enumerate(nums):
            curr += num
            if num * (right-left+1) - curr > k:
                curr -= nums[left]
                left += 1
        return len(nums) - left