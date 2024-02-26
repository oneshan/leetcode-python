# 2331 - Intersection of Multiple Arrays
# Date: 2022-09-27
# Runtime: 144 ms, Memory: 14.5 MB
# Submission Id: 809771947


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set.intersection(*[set(num) for num in nums])
        return sorted(ans)