# 1019 - Squares of a Sorted Array
# Date: 2022-09-15
# Runtime: 545 ms, Memory: 16.2 MB
# Submission Id: 800401758


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        buckets = [0] * 10001
        for num in nums:
            buckets[abs(num)] += 1
            
        ans = []
        for idx, count in enumerate(buckets):
            if count:
                ans.extend([idx ** 2] * count)
        return ans