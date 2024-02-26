# 3242 - Count Elements With Maximum Frequency
# Date: 2024-01-14
# Runtime: 37 ms, Memory: 17.4 MB
# Submission Id: 1145519798


from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        counter_of_freq = Counter(counter.values())
        
        freq = max(counter_of_freq)
        return freq * counter_of_freq[freq]