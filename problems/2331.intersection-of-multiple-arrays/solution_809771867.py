# 2331 - Intersection of Multiple Arrays
# Date: 2022-09-27
# Runtime: 86 ms, Memory: 14.6 MB
# Submission Id: 809771867


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set.intersection(*[set(num) for num in nums])
        return [num for num in range(1, 1001) if num in ans]