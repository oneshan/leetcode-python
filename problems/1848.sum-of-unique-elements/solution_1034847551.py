# 1848 - Sum of Unique Elements
# Date: 2023-08-29
# Runtime: 34 ms, Memory: 16.4 MB
# Submission Id: 1034847551


from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for num, count in counter.items():
            if count == 1:
                ans += num
        return ans