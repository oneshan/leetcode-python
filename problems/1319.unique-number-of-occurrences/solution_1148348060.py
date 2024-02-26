# 1319 - Unique Number of Occurrences
# Date: 2024-01-17
# Runtime: 37 ms, Memory: 17.6 MB
# Submission Id: 1148348060


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter) == len(set(counter.values()))