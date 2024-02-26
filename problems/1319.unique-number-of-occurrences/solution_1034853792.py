# 1319 - Unique Number of Occurrences
# Date: 2023-08-29
# Runtime: 37 ms, Memory: 16.6 MB
# Submission Id: 1034853792


from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter) == len(set(counter.values()))