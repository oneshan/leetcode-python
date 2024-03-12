# 3242 - Count Elements With Maximum Frequency
# Date: 2024-03-08
# Runtime: 51 ms, Memory: 16.5 MB
# Submission Id: 1197424785


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = max_freq = 0
        for freq in counter.values():
            if freq > max_freq:
                ans = freq
                max_freq = freq
            elif freq == max_freq:
                ans += freq
        return ans