# 3324 - Split the Array
# Date: 2024-02-25
# Runtime: 51 ms, Memory: 16.6 MB
# Submission Id: 1185311800


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for freq in counter.values():
            if freq > 2:
                return False
        return True