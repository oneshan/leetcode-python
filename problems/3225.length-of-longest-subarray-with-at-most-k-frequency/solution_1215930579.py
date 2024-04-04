# 3225 - Length of Longest Subarray With at Most K Frequency
# Date: 2024-03-28
# Runtime: 1264 ms, Memory: 32 MB
# Submission Id: 1215930579


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = Counter()
        left = ans = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            while counter[num] > k:
                counter[nums[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans