# 1256 - Rank Transform of an Array
# Date: 2023-10-26
# Runtime: 254 ms, Memory: 35.6 MB
# Submission Id: 1084547130


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        table = {}
        for idx, val in enumerate(sorted(set(arr)), 1):
            if val not in table:
                table[val] = idx
        return [table[val] for val in arr]