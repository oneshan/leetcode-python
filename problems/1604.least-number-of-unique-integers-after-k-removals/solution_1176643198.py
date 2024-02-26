# 1604 - Least Number of Unique Integers after K Removals
# Date: 2024-02-16
# Runtime: 296 ms, Memory: 33.3 MB
# Submission Id: 1176643198


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)

        n = len(arr)
        freqs = [0] * (n+1)
        for freq in counter.values():
            freqs[freq] += 1

        removed = 0
        for i in range(1, n+1):
            count_to_remove = min(k // i, freqs[i])
            k -= i * count_to_remove
            removed += count_to_remove
            if k < i:
                return len(counter) - removed
        return 0