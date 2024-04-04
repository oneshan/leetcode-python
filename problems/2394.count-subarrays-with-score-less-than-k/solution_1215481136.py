# 2394 - Count Subarrays With Score Less Than K
# Date: 2024-03-27
# Runtime: 818 ms, Memory: 31.1 MB
# Submission Id: 1215481136


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        curr = 0

        for right, num in enumerate(nums):
            curr += num
            while left <= right and curr * (right-left+1) >= k:
                curr -= nums[left]
                left += 1
            ans += (right-left+1)
        return ans