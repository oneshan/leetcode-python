# 0561 - Array Partition
# Date: 2022-07-14
# Runtime: 535 ms, Memory: 16.9 MB
# Submission Id: 746955187


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(num for idx, num in enumerate(sorted(nums), 1) if idx & 1)