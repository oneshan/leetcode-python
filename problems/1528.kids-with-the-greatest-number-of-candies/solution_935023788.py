# 1528 - Kids With the Greatest Number of Candies
# Date: 2023-04-17
# Runtime: 38 ms, Memory: 13.9 MB
# Submission Id: 935023788


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies) - extraCandies
        return [candy >= max_candy for candy in candies]