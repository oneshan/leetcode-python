# 2832 - Find the Longest Equal Subarray
# Date: 2024-05-31
# Runtime: 1348 ms, Memory: 33.5 MB
# Submission Id: 1273401617


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        counter = Counter()
        left = max_freq = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            max_freq = max(max_freq, counter[num])
            if right - left + 1 - max_freq > k:
                counter[nums[left]] -= 1
                left += 1
        return max_freq