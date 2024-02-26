# 0458 - Poor Pigs
# Date: 2023-10-29
# Runtime: 38 ms, Memory: 16.1 MB
# Submission Id: 1086612208


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        return ceil(log2(buckets) / log2(states))