# 1098 - Largest Unique Number
# Date: 2023-08-22
# Runtime: 57 ms, Memory: 16.6 MB
# Submission Id: 1028624543


from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for i in range(1000, -1, -1):
            if counter[i] == 1:
                return i
        return -1