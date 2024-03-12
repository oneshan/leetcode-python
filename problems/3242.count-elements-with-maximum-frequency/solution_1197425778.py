# 3242 - Count Elements With Maximum Frequency
# Date: 2024-03-08
# Runtime: 48 ms, Memory: 16.6 MB
# Submission Id: 1197425778


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        buckets = [0] * 101
        for num in nums:
            buckets[num] += 1

        ans = max_freq = 0
        for i in range(1, 101):
            freq = buckets[i]
            if freq > max_freq:
                ans = freq
                max_freq = freq
            elif freq == max_freq:
                ans += freq
        return ans