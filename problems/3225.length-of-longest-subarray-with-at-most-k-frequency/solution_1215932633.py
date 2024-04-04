# 3225 - Length of Longest Subarray With at Most K Frequency
# Date: 2024-03-28
# Runtime: 1190 ms, Memory: 30.9 MB
# Submission Id: 1215932633


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = Counter()
        left = 0
        chars_over_k = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            if counter[num] == k+1:
                chars_over_k += 1
            if chars_over_k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == k:
                    chars_over_k -= 1
                left += 1
        return len(nums) - left