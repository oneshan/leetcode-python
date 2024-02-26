# 1604 - Least Number of Unique Integers after K Removals
# Date: 2024-02-16
# Runtime: 310 ms, Memory: 33.3 MB
# Submission Id: 1176638626


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        freqs = list(counter.values())
        freqs.sort()

        removed = 0
        for idx, freq in enumerate(freqs):
            removed += freq
            if removed > k:
                return len(freqs) - idx
        return 0