# 1137 - Height Checker
# Date: 2022-11-26
# Runtime: 58 ms, Memory: 13.9 MB
# Submission Id: 850097619


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(e != h for e, h in zip(expected, heights))