# 1319 - Unique Number of Occurrences
# Date: 2022-09-27
# Runtime: 75 ms, Memory: 13.9 MB
# Submission Id: 809890874


from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        return len(set(freq.values())) == len(freq)